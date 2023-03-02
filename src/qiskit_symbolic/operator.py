"""Symbolic matrix operator module"""

import re
import numpy
from sympy import simplify
from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit.circuit import QuantumCircuit
from .library.standard_gates import IGate, XGate, YGate, ZGate, HGate, SGate, TGate


class Operator:
    """Symbolic matrix operator class"""

    def __init__(self, data):
        """todo"""
        # pylint: disable=duplicate-code
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

    @classmethod
    def from_label(cls, label):
        """todo"""
        char2matrix = {
            'I': IGate().to_sympy(),
            'X': XGate().to_sympy(),
            'Y': YGate().to_sympy(),
            'Z': ZGate().to_sympy(),
            'H': HGate().to_sympy(),
            'S': SGate().to_sympy(),
            'T': TGate().to_sympy()
        }
        if re.match(r'^[IXYZHST]+$', label) is None:
            raise ValueError
        one_qubit_ops = [char2matrix[char] for char in label]
        data = TensorProduct(*one_qubit_ops)
        return cls(data=data)

    def to_sympy(self):
        """todo"""
        return self._data

    def to_numpy(self):
        """todo"""
        try:
            return numpy.array(self.to_sympy(), dtype=complex)
        except TypeError:
            return numpy.array(self.to_sympy(), dtype=object)

    def is_unitary(self):
        """todo"""
        matrix = simplify(self.dagger().to_sympy() @ self.to_sympy())
        identity = numpy.eye(matrix.shape[0])
        try:
            numpy_matrix = numpy.array(matrix, dtype=complex)
            return numpy.allclose(numpy_matrix, identity)
        except TypeError:
            return False

    def is_valid(self):
        """todo"""
        return self.is_unitary()

    def transpose(self):
        """todo"""
        return self.__class__(self.to_sympy().transpose())

    def conjugate(self):
        """todo"""
        return self.__class__(self.to_sympy().conjugate())

    def dagger(self):
        """todo"""
        return self.__class__(self.to_sympy().transpose().conjugate())

    def dot(self, other):
        """todo"""
        if not isinstance(other, Operator):
            other = Operator(other)
        dotprod = self.to_sympy() @ other.to_sympy()
        return self.__class__(dotprod)
