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
