"""Symbolic quantum statevector module"""

import string
import numpy
import sympy
import opt_einsum
from qiskit import QuantumCircuit, transpile
from qiskit.converters import circuit_to_dag


def get_einsum_contract(tensor, *gates):
    """todo"""
    num_qubits = tensor.rank()
    in_indices = string.ascii_lowercase[:num_qubits]
    qubits = [gate.qubits[0] for gate in gates]
    ops_indices = ', '.join(
        [in_indices[-(i+1)].upper() + in_indices[-(i+1)] for i in qubits])
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
        from ..circuit.gate import Gate
        nq = circuit.num_qubits
        circuit = QuantumCircuit(nq).compose(circuit)
        circuit = transpile(circuit, optimization_level=1)
        zero = [1] + [0] * (2**nq - 1)
        tensor = sympy.Array(zero, shape=(2,)*nq)
        for layer in circuit_to_dag(circuit).layers():
            symb_gates = [Gate.get(gate_node=gate_node)
                          for gate_node in layer['graph'].gate_nodes()]
            einsum_contract = get_einsum_contract(tensor, *symb_gates)
            gates = [gate.to_sympy() for gate in symb_gates]
            tensor = opt_einsum.contract(einsum_contract, tensor, *gates)
        gph = sympy.exp(sympy.I * circuit.global_phase)
        state = gph * sympy.Array(tensor, shape=(2**nq,))
        return state

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

    def to_lambda(self):
        """todo"""
        sympy_expr = self.to_sympy()
        name2symb = {symb.name: symb for symb in sympy_expr.free_symbols}
        args = [name2symb[par.name]
                if par.name in name2symb
                else sympy.Symbol('_')
                for par in self._params]
        return sympy.lambdify(args=args, expr=sympy_expr, modules='numpy', dummify=True, cse=True)

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
