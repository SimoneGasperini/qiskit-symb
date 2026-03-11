"""Symbolic simulator module."""

import numpy
import sympy
from qiskit.circuit import ParameterVector
from .quantum_info.mpo import _layers_to_symbolic_gates, _preprocess_circuit


def _flat_params_dict(params_dict):
    """Expand ParameterVector keys into scalar parameter entries."""
    flat_params = {}
    for param, param_values in params_dict.items():
        if isinstance(param, ParameterVector):
            for scalar_param, scalar_values in zip(param, zip(*param_values)):
                flat_params[scalar_param] = scalar_values
        else:
            flat_params[param] = param_values
    return flat_params


class CompiledCircuit:
    """Executable compiled gates for repeated statevector evaluations."""

    def __init__(self, num_qubits, gates, global_phase):
        """Store compiled data used by Simulator.run()."""
        self.num_qubits = num_qubits
        self.gates = gates
        self.global_phase = global_phase


def _gate_matrix(gate):
    """Return symbolic matrix representation of one gate."""
    dim = 2**gate.nqubits
    return numpy.array(gate._get_tensor_array().tolist(), dtype=object).reshape(
        dim, dim
    )


def _build_blocks(gates, max_block_qubits, max_block_gates):
    """Fuse consecutive gates on the same qubits into small compilation blocks."""
    blocks = []
    current_qubits = None
    current_gates = []
    for gate in gates:
        gate_qubits = tuple(gate.qubits)
        must_start_new_block = (
            not current_gates
            or gate_qubits != current_qubits
            or len(current_gates) >= max_block_gates
            or len(gate_qubits) > max_block_qubits
        )
        if must_start_new_block:
            if current_gates:
                blocks.append((current_qubits, current_gates))
            current_qubits = gate_qubits
            current_gates = [gate]
        else:
            current_gates.append(gate)
    if current_gates:
        blocks.append((current_qubits, current_gates))
    return blocks


def _compile_block(block_qubits, block_gates, ordered_params):
    """Return compiled block data as tuple: (matrix_or_func, args_or_none, qubits, dim)."""
    dim = 2 ** len(block_qubits)
    block_matrix = numpy.eye(dim, dtype=object)
    for gate in block_gates:
        block_matrix = _gate_matrix(gate) @ block_matrix
    sympy_matrix = sympy.Array(block_matrix.tolist())
    free_symbols = sympy_matrix.free_symbols
    if not free_symbols:
        const_matrix = numpy.array(block_matrix, dtype=complex)
        return const_matrix, None, block_qubits, dim

    name2symb = {symb.name: symb for symb in free_symbols}
    args = tuple(par for par in ordered_params if par.name in name2symb)
    sympy_args = [name2symb[par.name] for par in args]
    func = sympy.lambdify(
        args=sympy_args, expr=sympy_matrix, modules="numpy", dummify=True, cse=True
    )
    return func, args, block_qubits, dim


def _compile_global_phase(phase_expr, ordered_params):
    """Return (value_or_func, args_or_none) for a circuit global phase."""
    phase = sympy.exp(sympy.I * phase_expr)
    free_symbols = phase.free_symbols
    if not free_symbols:
        return complex(phase), None

    name2symb = {symb.name: symb for symb in free_symbols}
    args = tuple(par for par in ordered_params if par.name in name2symb)
    sympy_args = [name2symb[par.name] for par in args]
    func = sympy.lambdify(
        args=sympy_args, expr=phase, modules="numpy", dummify=True, cse=True
    )
    return func, args


def _apply_gate_matrix_to_state(state, matrix, qubits, num_qubits, gate_dim):
    """Apply a k-qubit matrix to a full statevector."""
    tensor = state.reshape((2,) * num_qubits)
    gate_axes = [num_qubits - 1 - qubit for qubit in qubits]
    keep_axes = [axis for axis in range(num_qubits) if axis not in gate_axes]
    perm = keep_axes + gate_axes
    inv_perm = numpy.argsort(perm)
    permuted = numpy.transpose(tensor, perm)
    flat = permuted.reshape(-1, gate_dim)
    updated = flat @ matrix.T
    return numpy.transpose(updated.reshape(permuted.shape), inv_perm).reshape(
        2**num_qubits
    )


class Simulator:
    """Symbolic simulator for repeated circuit evaluations."""

    def __init__(self, max_block_qubits=4, max_block_gates=6):
        """Create a simulator with lightweight same-qubit gate fusion."""
        self._max_block_qubits = max_block_qubits
        self._max_block_gates = max_block_gates

    @staticmethod
    def _run_once(compiled_circ, arg_values):
        """Evaluate one parameter assignment and return the output statevector."""
        num_qubits = compiled_circ.num_qubits
        state = numpy.zeros(2**num_qubits, dtype=complex)
        state[0] = 1.0
        for matrix_or_func, args_or_none, qubits, dim in compiled_circ.gates:
            if args_or_none is None:
                matrix = matrix_or_func
            else:
                matrix = numpy.array(
                    matrix_or_func(*(arg_values[arg] for arg in args_or_none)),
                    dtype=complex,
                ).reshape(dim, dim)
            state = _apply_gate_matrix_to_state(
                state=state,
                matrix=matrix,
                qubits=qubits,
                num_qubits=num_qubits,
                gate_dim=dim,
            )
        phase_or_func, phase_args = compiled_circ.global_phase
        if phase_args is None:
            state = phase_or_func * state
        else:
            state = phase_or_func(*(arg_values[arg] for arg in phase_args)) * state
        return state

    def compile(self, circ):
        """Compile a circuit into reusable symbolic gate evaluators."""
        transpiled_circ = _preprocess_circuit(circ)
        symbolic_layers = _layers_to_symbolic_gates(transpiled_circ)
        gates = []
        for layer in symbolic_layers:
            gates.extend(layer)
        blocks = _build_blocks(
            gates=gates,
            max_block_qubits=self._max_block_qubits,
            max_block_gates=self._max_block_gates,
        )
        params = tuple(circ.parameters)
        compiled_gates = []
        for block_qubits, block_gates in blocks:
            compiled_gates.append(
                _compile_block(
                    block_qubits=block_qubits,
                    block_gates=block_gates,
                    ordered_params=params,
                )
            )
        return CompiledCircuit(
            num_qubits=circ.num_qubits,
            gates=compiled_gates,
            global_phase=_compile_global_phase(
                phase_expr=transpiled_circ.global_phase, ordered_params=params
            ),
        )

    def run(self, compiled_circ, params_dict):
        """Evaluate a compiled circuit for multiple parameter assignments."""
        flat_params = _flat_params_dict(params_dict=params_dict)
        num_reps = len(next(iter(flat_params.values()))) if flat_params else 1
        results = []
        for i in range(num_reps):
            arg_values = {}
            for arg, values in flat_params.items():
                arg_values[arg] = values[i]
            results.append(
                self._run_once(compiled_circ=compiled_circ, arg_values=arg_values)
            )
        return results
