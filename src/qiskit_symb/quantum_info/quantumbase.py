"""Symbolic quantum base module"""

import functools
import operator
import sympy
from sympy.physics.quantum.operator import IdentityOperator
from qiskit.circuit import QuantumCircuit
from qiskit.converters import circuit_to_dag


class QuantumBase:
    """Abstract symbolic quantum base class"""

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
    def _get_unitary(circuit):
        """todo"""
        from ..circuit.gate import Gate
        circuit = QuantumCircuit(circuit.num_qubits).compose(circuit)
        gphase_term = sympy.exp(sympy.I * circuit.global_phase)
        identity = IdentityOperator(circuit.num_qubits**2)
        symb_gates = [Gate.get(gate_node=gate_node)
                      for layer in circuit_to_dag(circuit).layers()
                      for gate_node in layer['graph'].gate_nodes()]
        symb_unitary = gphase_term * functools.reduce(
            operator.mul, symb_gates[::-1], identity)
        return symb_unitary

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
        return sympy.matrix2numpy(self.to_sympy(), dtype=complex)

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
