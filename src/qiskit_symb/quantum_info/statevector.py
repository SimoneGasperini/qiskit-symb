"""Symbolic quantum statevector module"""

import string
import itertools
import numpy
import sympy
import opt_einsum
from qiskit import QuantumCircuit, transpile
from qiskit.converters import circuit_to_dag


def get_einsum_contract(state, gates):
    """todo"""
    num_qubits = len(state.shape)
    in_indices = string.ascii_lowercase[:num_qubits]
    gates_qubits = [gate.qubits for gate in gates]
    ops_indices = ', '.join(''.join(in_indices[-(q+1)].upper() for q in qubits) +
                            ''.join(in_indices[-(q+1)] for q in qubits)
                            for qubits in gates_qubits)
    qubits = set(itertools.chain.from_iterable(gates_qubits))
    out_indices = ''.join(
        [x.upper() if i in qubits else x for i, x in enumerate(in_indices[::-1])])
    einsum_contract = f'{in_indices}, {ops_indices} -> {out_indices[::-1]}'
    return einsum_contract


class Statevector:
    """Symbolic quantum statevector class"""

    def __init__(self, data, nqubits=None, params=None):
        """todo"""
        if isinstance(data, QuantumCircuit):
            nqubits = data.num_qubits
            params = tuple(data.parameters)
            data = self._get_sympy_expr(circuit=data)
        self._sympy_expr = data
        self._nqubits = nqubits
        self._params = params

    @staticmethod
    def _get_sympy_expr(circuit):
        """todo"""
        from ..circuit import get_gates
        from ..circuit.gate import Gate
        num_qubits = circuit.num_qubits
        circuit = QuantumCircuit(num_qubits).compose(circuit)
        basis_gates = get_gates()
        circuit = transpile(
            circuit, basis_gates=basis_gates, optimization_level=1)
        zero = [1] + [0] * (2**num_qubits - 1)
        state_tensor = sympy.Array(zero, shape=(2,)*num_qubits)
        for layer in circuit_to_dag(circuit).layers():
            gates = [Gate.get(gate_node=gate_node)
                     for gate_node in layer['graph'].gate_nodes()]
            einsum_contract = get_einsum_contract(state_tensor, gates)
            gates_tensors = [gate._get_tensor_array() for gate in gates]
            state_tensor = opt_einsum.contract(
                einsum_contract, state_tensor, *gates_tensors)
        gph = sympy.exp(sympy.I * circuit.global_phase)
        state_tensor = gph * sympy.Array(state_tensor, shape=2**num_qubits)
        return state_tensor

    @classmethod
    def from_circuit(cls, circuit):
        """todo"""
        sympy_expr = cls._get_sympy_expr(circuit=circuit)
        nqubits = circuit.num_qubits
        params = tuple(circuit.parameters)
        return cls(data=sympy_expr, nqubits=nqubits, params=params)

    @classmethod
    def from_sympy_expr(cls, sympy_expr, nqubits, params):
        """todo"""
        return cls(data=sympy_expr, nqubits=nqubits, params=params)

    def to_sympy(self, simplify=False):
        """todo"""
        return sympy.simplify(self._sympy_expr) if simplify else self._sympy_expr

    def to_numpy(self):
        """todo"""
        return numpy.array(self.to_sympy().tolist(), dtype=complex)

    def _lambdify(self, sympy_expr):
        """todo"""
        name2symb = {symb.name: symb for symb in sympy_expr.free_symbols}
        args = [name2symb[par.name]
                if par.name in name2symb
                else sympy.Symbol('_')
                for par in self._params]
        return sympy.lambdify(args=args, expr=sympy_expr, modules='numpy', dummify=True, cse=True)

    def to_lambda(self):
        """todo"""
        sympy_expr = self.to_sympy()
        return self._lambdify(sympy_expr=sympy_expr)

    def subs(self, params_dict):
        """todo"""
        par2val = {}
        for par, val in params_dict.items():
            if hasattr(par, '__len__'):
                par2val.update(dict(zip(par, val)))
            else:
                par2val[par] = val
        sympy_expr = self.to_sympy()
        name2symb = {symb.name: symb for symb in sympy_expr.free_symbols}
        symb2val = {name2symb[par.name]: val for par, val in par2val.items()
                    if par.name in name2symb}
        params = [par for par in self._params if par not in par2val]
        return self.from_sympy_expr(sympy_expr.subs(symb2val),
                                    nqubits=self._nqubits, params=params)
