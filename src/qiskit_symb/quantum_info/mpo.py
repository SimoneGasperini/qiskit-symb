"""Shared symbolic MPO/TN evaluation backend."""

import numpy
import sympy
from qiskit import QuantumCircuit, transpile
from qiskit.converters import circuit_to_dag


def _preprocess_circuit(circuit):
    """Build a normalized and transpiled copy of the input circuit."""
    from ..circuit import build_target

    num_qubits = circuit.num_qubits
    normalized = QuantumCircuit(num_qubits).compose(circuit)
    return transpile(normalized, target=build_target(), optimization_level=1)


def _layers_to_symbolic_gates(circuit):
    """Convert transpiled circuit layers to symbolic gates."""
    from ..circuit.gate import Gate

    layers = []
    for layer in circuit_to_dag(circuit).layers():
        gates = [Gate.get(gate_node) for gate_node in layer["graph"].gate_nodes()]
        if gates:
            layers.append(gates)
    return layers


def _gate_matrix_and_kind(gate):
    """Return gate matrix plus a cheap structural classification."""
    k = gate.nqubits
    dim = 2**k
    gate_tensor = gate._get_tensor_array()
    mat = numpy.array(gate_tensor.tolist(), dtype=object).reshape(dim, dim)
    diagonal = True
    for row in range(dim):
        for col in range(dim):
            if row != col and not sympy.sympify(mat[row, col]) == 0:
                diagonal = False
                break
        if not diagonal:
            break
    if diagonal:
        diag = numpy.array([mat[i, i] for i in range(dim)], dtype=object)
        return mat, ("diagonal", diag)
    col_used = [0] * dim
    perm = []
    coeffs = []
    monomial = True
    for row in range(dim):
        nz_cols = [col for col in range(dim) if not sympy.sympify(mat[row, col]) == 0]
        if len(nz_cols) != 1:
            monomial = False
            break
        col = nz_cols[0]
        col_used[col] += 1
        if col_used[col] > 1:
            monomial = False
            break
        perm.append(col)
        coeffs.append(mat[row, col])
    if monomial and all(count == 1 for count in col_used):
        return mat, ("monomial", numpy.array(perm), numpy.array(coeffs, dtype=object))
    return mat, ("generic",)


def _apply_gate_to_axes(tensor, gate, num_row_axes):
    """Apply a k-qubit gate on selected row axes of a tensor."""
    gate_matrix, kind = _gate_matrix_and_kind(gate)
    qubits = gate.qubits
    gate_axes = [num_row_axes - 1 - qubit for qubit in qubits]
    k = len(gate_axes)
    dim = 2**k
    total_axes = tensor.ndim
    keep_axes = [axis for axis in range(total_axes) if axis not in gate_axes]
    perm = keep_axes + gate_axes
    inv_perm = numpy.argsort(perm)
    permuted = numpy.transpose(tensor, perm)
    flat = permuted.reshape(-1, dim)
    if kind[0] == "diagonal":
        flat = flat * kind[1]
    elif kind[0] == "monomial":
        flat = flat[:, kind[1]] * kind[2]
    else:
        flat = flat @ gate_matrix.T
    updated = flat.reshape(permuted.shape)
    return numpy.transpose(updated, inv_perm)


class MPOFramework:
    """Common symbolic backend for statevector and operator construction."""

    @staticmethod
    def build_statevector(circuit):
        """Return symbolic statevector for circuit."""
        circuit = _preprocess_circuit(circuit)
        num_qubits = circuit.num_qubits
        layers = _layers_to_symbolic_gates(circuit)
        state_tensor = numpy.zeros((2,) * num_qubits, dtype=object)
        state_tensor[(0,) * num_qubits] = 1
        for gates in layers:
            for gate in gates:
                state_tensor = _apply_gate_to_axes(
                    tensor=state_tensor, gate=gate, num_row_axes=num_qubits
                )
        gphase = sympy.exp(sympy.I * circuit.global_phase)
        state = sympy.Array(state_tensor.reshape(2**num_qubits))
        return gphase * state

    @staticmethod
    def build_operator(circuit):
        """Return symbolic operator for circuit."""
        circuit = _preprocess_circuit(circuit)
        num_qubits = circuit.num_qubits
        layers = _layers_to_symbolic_gates(circuit)
        dim = 2**num_qubits
        op_tensor = numpy.eye(dim, dtype=object).reshape((2,) * (2 * num_qubits))
        for gates in layers:
            for gate in gates:
                op_tensor = _apply_gate_to_axes(
                    tensor=op_tensor, gate=gate, num_row_axes=num_qubits
                )
        gphase = sympy.exp(sympy.I * circuit.global_phase)
        op = sympy.Array(op_tensor.reshape(dim, dim))
        return gphase * op
