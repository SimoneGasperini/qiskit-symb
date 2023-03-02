""""Symbolic quantum state module"""

import re
import numpy
from sympy.matrices import Matrix
from qiskit.circuit import QuantumCircuit


class QuantumState:
    """Abstract symbolic quantum state base class"""

    def __init__(self, data):
        """todo"""
        if isinstance(data, Matrix):
            self._data = data
        elif isinstance(data, (list, numpy.ndarray)):
            self._data = Matrix(data)
        elif isinstance(data, QuantumCircuit):
            raise NotImplementedError
        elif isinstance(data, type(self)):
            self._data = data._data
        else:
            raise TypeError

    @staticmethod
    def _init_data(label):
        """todo"""
        if re.match(r'^[01]+$', label) is None:
            raise ValueError
        num_qubits = len(label)
        data = numpy.zeros(1 << num_qubits, dtype=int)
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
        if not numpy.isscalar(fact):
            raise TypeError
        return self.__class__(self._data * fact)

    def __rmul__(self, fact):
        """todo"""
        return self.__mul__(fact)

    def __truediv__(self, div):
        """todo"""
        if not numpy.isscalar(div):
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
