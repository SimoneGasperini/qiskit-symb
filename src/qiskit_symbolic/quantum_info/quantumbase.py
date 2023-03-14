"""Symbolic quantum base module"""

import re
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
        elif isinstance(data, type(self)):
            self._data = data._data
        else:
            raise TypeError

    @staticmethod
    def _init_from_label(label):
        """todo"""
        if re.match(r'^[01]+$', label) is None:
            raise ValueError
        num_qubits = len(label)
        data = np.zeros(1 << num_qubits, dtype=int)
        data[int(label, 2)] = 1
        return data

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
                        for par, value in params_dict.items()}
        return self.__class__(sympy_matrix.subs(symbol2value))
