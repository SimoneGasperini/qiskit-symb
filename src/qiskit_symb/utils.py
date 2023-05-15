"""Utilities module"""

import random
from sympy import Symbol, sympify
from qiskit import QuantumCircuit, transpile
from qiskit.transpiler.passes import RemoveBarriers
from .circuit.library import NAME_TO_INIT  # pylint: disable=cyclic-import


def get_init(name):
    """todo"""
    if name not in NAME_TO_INIT:
        raise NotImplementedError(
            f'Gate "{name}" is not implemented in qiskit-symb')
    return NAME_TO_INIT[name]


def get_symbolic_gates_names():
    """todo"""
    return set(NAME_TO_INIT.keys())


def flatten_circuit(circuit):
    """todo"""
    qubits, clbits = circuit.num_qubits, circuit.num_clbits
    return QuantumCircuit(qubits, clbits).compose(circuit)


def transpile_circuit(circuit):
    """todo"""
    circuit = RemoveBarriers()(circuit)
    return transpile(circuit, optimization_level=2)


def get_symbolic_expr(par_expr):
    """todo"""
    # pylint: disable=protected-access
    if hasattr(par_expr, '_symbol_expr'):
        return sympify(par_expr._symbol_expr)
    return par_expr


def get_unique_symbols(par_expr):
    """todo"""
    # pylint: disable=protected-access
    if hasattr(par_expr, '_parameter_symbols'):
        return list(dict.fromkeys([sympify(symb) for symb in par_expr._parameter_symbols.values()]))
    return []


def symbols2real(sympy_expr):
    """todo"""
    args_dict = {symbol: Symbol(symbol.name, real=True)
                 for symbol in sympy_expr.free_symbols}
    return sympy_expr.subs(args_dict)


def get_random_params(params_dict, size, seed=None):
    """todo"""
    random.seed(seed)
    parnames = list(params_dict.keys())
    params = list(zip(*[[random.randint(*params_dict[parname]) for _ in range(size)]
                        for parname in parnames]))
    ids = [','.join([f'{parname}={parval}'
                     for parname, parval in zip(parnames, parvals)])
           for parvals in params]
    return params, ids


def get_random_controlled(base_gate, seed=None):
    """todo"""
    random.seed(seed)
    num_targets = base_gate.num_qubits
    num_controls = random.randint(1, 3)
    state = random.randint(0, num_controls)
    ctrl_state = format(state, 'b').zfill(num_controls)
    gate = base_gate.control(num_controls, ctrl_state=ctrl_state)
    num_qubits = num_controls + num_targets
    num_wires = random.randint(num_qubits, num_qubits+1)
    qargs = random.sample(range(num_wires), num_qubits)
    circuit = QuantumCircuit(num_wires)
    circuit.append(gate, qargs)
    return circuit
