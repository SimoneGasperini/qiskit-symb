"""Symbolic statevector module"""

import re
import numpy
import sympy
from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit.circuit import QuantumCircuit


class Statevector:
    """Symbolic statevector class"""

    def __init__(self, data):
        """todo"""
        if isinstance(data, Matrix):
            self._data = data
        elif isinstance(data, (list, numpy.ndarray)):
            self._data = Matrix(data)
        elif isinstance(data, QuantumCircuit):
            self._data = self.from_circuit(data)
        elif isinstance(data, type(self)):
            self._data = data._data
        else:
            raise TypeError

    def __len__(self):
        """todo"""
        return len(self._data)

    @classmethod
    def from_label(cls, label):
        """todo"""
        if re.match(r'^[01]+$', label) is None:
            raise ValueError
        num_qubits = len(label)
        data = numpy.zeros(1 << num_qubits, dtype=int)
        data[int(label, 2)] = 1
        return cls(data=data)

    @classmethod
    def from_circuit(cls, circuit):
        """todo"""
        return circuit

    def to_sympy(self):
        """todo"""
        return self._data

    def to_numpy(self, dtype=object):
        """todo"""
        return numpy.array(self.to_sympy())[:, 0].astype(dtype=dtype)

    def is_valid(self):
        """todo"""
        try:
            norm = numpy.linalg.norm(self.to_numpy(dtype=complex))
            return numpy.allclose(norm, 1)
        except TypeError:
            norm = sympy.sqrt(self.inner(self)).simplify()
            return norm == 1

    def transpose(self):
        """todo"""
        return self.__class__(self.to_sympy().transpose())

    def conjugate(self):
        """todo"""
        return self.__class__(self.to_sympy().conjugate())

    def dagger(self):
        """todo"""
        return self.__class__(self.to_sympy().transpose().conjugate())

    def tensor(self, other):
        """todo"""
        if not isinstance(other, Statevector):
            other = Statevector(other)
        tensorprod = TensorProduct(self.to_sympy(), other.to_sympy())
        return self.__class__(tensorprod)

    def inner(self, other):
        """todo"""
        if not isinstance(other, Statevector):
            other = Statevector(other)
        if len(self) != len(other):
            raise ValueError
        return self.to_sympy().dot(other.to_sympy())

    def outer(self, other):
        """todo"""
        if not isinstance(other, Statevector):
            other = Statevector(other)
        if len(self) != len(other):
            raise ValueError
        return self.to_sympy() * other.to_sympy().T

    def projector(self):
        """todo"""
        return self.outer(self)
