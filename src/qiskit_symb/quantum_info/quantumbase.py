"""Symbolic quantum base module"""

import functools
import operator
import numpy
import sympy
from sympy.physics.quantum import IdentityOperator, represent
from qiskit import QuantumCircuit, transpile
from qiskit.converters import circuit_to_dag


class QuantumBase:
    """Abstract symbolic quantum base class"""

    def __init__(self, data, nqubits=None, params=None):
        """todo"""
        if isinstance(data, QuantumCircuit):
            nqubits = data.num_qubits
            params = tuple(data.parameters)
            data = self._get_data(circuit=data)
        self._data = data
        self._nqubits = nqubits
        self._params = params

    @staticmethod
    def _get_unitary(circuit):
        """todo"""
        from ..circuit.gate import Gate
        from ..circuit import basis_gates
        circuit = QuantumCircuit(circuit.num_qubits).compose(circuit)
        circuit = transpile(
            circuit, basis_gates=basis_gates, optimization_level=1)
        gphase_term = sympy.exp(sympy.I * circuit.global_phase)
        identity = IdentityOperator(circuit.num_qubits**2)
        symb_gates = [Gate.get(gate_node=gate_node)
                      for layer in circuit_to_dag(circuit).layers()
                      for gate_node in layer['graph'].gate_nodes()]
        symb_unitary = functools.reduce(
            operator.mul, symb_gates[::-1], identity)
        return gphase_term * symb_unitary

    @classmethod
    def from_circuit(cls, circuit):
        """todo"""
        data = cls._get_data(circuit=circuit)
        nqubits = circuit.num_qubits
        params = tuple(circuit.parameters)
        return cls(data=data, nqubits=nqubits, params=params)

    @classmethod
    def from_data(cls, data, nqubits, params):
        """todo"""
        return cls(data=data, nqubits=nqubits, params=params)

    def _repr_latex_(self):
        """todo"""
        return self._data._repr_latex_()

    def to_sympy(self):
        """todo"""
        return represent(self._data, nqubits=self._nqubits)

    def to_numpy(self):
        """todo"""
        return sympy.matrix2numpy(self.to_sympy(), dtype=complex)

    def to_lambda(self):
        """todo"""
        matrix = self.to_sympy()
        name2symb = {symb.name: symb for symb in matrix.free_symbols}
        args = [name2symb[par.name] if par.name in name2symb else sympy.Symbol('_')
                for par in self._params]
        return sympy.lambdify(args=args, expr=matrix, modules='numpy', dummify=True, cse=True)

    def subs(self, params_dict):
        """todo"""
        par2val = {}
        for par, val in params_dict.items():
            if hasattr(par, '__len__'):
                par2val.update(dict(zip(par, val)))
            else:
                par2val[par] = val
        matrix = self.to_sympy()
        name2symb = {symb.name: symb for symb in matrix.free_symbols}
        symb2val = {name2symb[par.name]: val for par, val in par2val.items()
                    if par.name in name2symb}
        data = matrix.subs(symb2val)
        nqubits = int(numpy.log2(len(data)))
        params = [par for par in self._params if par not in par2val]
        return self.from_data(data=data, nqubits=nqubits, params=params)
