"""Symbolic quantum base module"""

import numpy as np
from sympy.matrices import Matrix
from qiskit.circuit import QuantumCircuit


class QuantumBase:
    """Abstract symbolic quantum base class"""

    def __init__(self, data):
        """todo"""
        # pylint: disable=no-member
        if isinstance(data, Matrix):
            self._data = data
        elif isinstance(data, (list, np.ndarray)):
            self._data = Matrix(data)
        elif isinstance(data, QuantumCircuit):
            self._data = self._init_from_circuit(data)
        else:
            raise TypeError

    @classmethod
    def from_label(cls, label):
        """todo"""
        # pylint: disable=no-member
        data = cls._init_from_label(label)
        return cls(data=data)

    @classmethod
    def from_circuit(cls, circuit):
        """todo"""
        # pylint: disable=no-member
        data = cls._init_from_circuit(circuit)
        return cls(data=data)

    @staticmethod
    def _get_circ_data(circuit):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=cyclic-import
        # pylint: disable=protected-access
        from ..utils import get_layers_data
        from ..circuit import Gate, ControlledGate
        from ..circuit.library import IGate
        layers_data = get_layers_data(circuit)
        num_qubits, num_layers = circuit.num_qubits, len(layers_data)
        circ_data = [[IGate()] * num_qubits for _ in range(num_layers)]
        for layer_idx in range(num_layers):
            for instruction in layers_data[layer_idx]:
                gate = Gate.get(instruction)
                if isinstance(gate, ControlledGate):
                    gate_span = gate._span
                    qubit_idx = gate_span[0]
                    for i in gate_span[1:]:
                        circ_data[layer_idx][i] = None
                else:
                    qubit_idx = instruction.qargs[0]._index
                circ_data[layer_idx][qubit_idx] = gate
        return circ_data

    def __add__(self, other):
        """todo"""
        if not isinstance(other, type(self)):
            raise TypeError
        return self.__class__(self._data + other._data)

    def __neg__(self):
        """todo"""
        return self.__class__(-self._data)

    def __sub__(self, other):
        """todo"""
        if not isinstance(other, type(self)):
            raise TypeError
        return self.__class__(self._data - other._data)

    def __mul__(self, fact):
        """todo"""
        if not np.isscalar(fact):
            raise TypeError
        return self.__class__(self._data * fact)

    def __rmul__(self, fact):
        """todo"""
        return self.__mul__(fact)

    def __truediv__(self, div):
        """todo"""
        if not np.isscalar(div):
            raise TypeError
        return self.__class__(self._data / div)

    def to_sympy(self):
        """todo"""
        return self._data

    def transpose(self):
        """todo"""
        return self.__class__(self.to_sympy().transpose())

    def conjugate(self):
        """todo"""
        return self.__class__(self.to_sympy().conjugate())

    def dagger(self):
        """todo"""
        return self.__class__(self.to_sympy().transpose().conjugate())

    def subs(self, params_dict):
        """todo"""
        sympy_matrix = self.to_sympy()
        name2symbol = {symbol.name: symbol
                       for symbol in sympy_matrix.free_symbols}
        symbol2value = {name2symbol[par.name]: value
                        for par, value in params_dict.items()
                        if par.name in name2symbol}
        return self.__class__(sympy_matrix.subs(symbol2value))
