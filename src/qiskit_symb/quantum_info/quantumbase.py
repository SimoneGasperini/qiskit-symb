"""Symbolic quantum base module"""

import sympy
from sympy import lambdify, Symbol
from sympy.core.rules import Transform
from sympy.matrices import matrix2numpy
from qiskit import QuantumCircuit


class QuantumBase:
    """Abstract symbolic quantum base class"""

    def __init__(self, data, params):
        """todo"""
        # pylint: disable=no-member
        if isinstance(data, QuantumCircuit):
            params = list(data.parameters)
            data = self._get_data_from_circuit(circuit=data)
        self._data = data
        self._params = params

    @staticmethod
    def _get_circ_data(circuit):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        # pylint: disable=too-many-locals
        from ..utils import flatten_circuit, transpile_circuit
        from ..circuit import Gate
        from ..circuit.library import IGate
        circuit = transpile_circuit(flatten_circuit(circuit))
        gph = sympy.exp(sympy.I * circuit.global_phase)
        layers_data = circuit.draw(output='text').nodes
        num_qubits, num_layers = circuit.num_qubits, len(layers_data)
        circ_data = [[IGate()] * num_qubits for _ in range(num_layers)]
        for layer_idx in range(num_layers):
            for instruction in layers_data[layer_idx]:
                gate = Gate.get(instruction)
                if gate.num_qubits > 1:
                    gate_span = gate._span
                    qubit_idx = gate_span[0]
                    for i in gate_span[1:]:
                        circ_data[layer_idx][i] = None
                else:
                    qubit_idx = instruction.qargs[0]._index
                circ_data[layer_idx][qubit_idx] = gate
        return gph, circ_data

    @classmethod
    def from_label(cls, label):
        """todo"""
        # pylint: disable=no-member
        data = cls._get_data_from_label(label)
        return cls(data=data, params=[])

    @classmethod
    def from_circuit(cls, circuit):
        """todo"""
        # pylint: disable=no-member
        data = cls._get_data_from_circuit(circuit)
        params = list(circuit.parameters)
        return cls(data=data, params=params)

    def to_sympy(self):
        """todo"""
        # pylint: disable=unnecessary-lambda
        sympy_matrix = self._data
        sympy_matrix = sympy_matrix.xreplace(
            Transform(lambda x: x.round(3), lambda x: x.is_Float))
        sympy_matrix = sympy_matrix.xreplace(
            Transform(lambda x: int(x), lambda x: x.is_Float and x == int(x)))
        return sympy_matrix

    def to_numpy(self):
        """todo"""
        return matrix2numpy(self._data, dtype=complex)

    def to_lambda(self):
        """todo"""
        sympy_matrix = self._data
        name2symb = {symb.name: symb for symb in sympy_matrix.free_symbols}
        args = [name2symb[par.name] if par.name in name2symb else Symbol('_')
                for par in self._params]
        return lambdify(args=args, expr=sympy_matrix, modules='numpy', dummify=True, cse=True)

    def subs(self, params_dict):
        """todo"""
        par2val = {}
        for par, val in params_dict.items():
            if hasattr(par, '__len__'):
                par2val.update(dict(zip(par, val)))
            else:
                par2val[par] = val
        sympy_matrix = self._data
        name2symb = {symb.name: symb for symb in sympy_matrix.free_symbols}
        symb2val = {name2symb[par.name]: val for par, val in par2val.items()
                    if par.name in name2symb}
        data = sympy_matrix.subs(symb2val)
        params = [par for par in self._params if par not in par2val]
        return self.__class__(data=data, params=params)

    def transpose(self):
        """todo"""
        return self.__class__(data=self._data.T, params=self._params)

    def conjugate(self):
        """todo"""
        return self.__class__(data=self._data.conjugate(), params=self._params)

    def dagger(self):
        """todo"""
        return self.__class__(data=self._data.T.conjugate(), params=self._params)
