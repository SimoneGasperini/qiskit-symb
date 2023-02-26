"""Symbolic statevector module"""

import numpy
import sympy
from sympy.physics.quantum import TensorProduct
from .quantumstate import QuantumState


class Statevector(QuantumState):
    """Symbolic statevector class"""

    def __init__(self, data):
        """todo"""
        super().__init__(data=data)

    def __len__(self):
        """todo"""
        return len(self._data)

    @classmethod
    def from_label(cls, label):
        """todo"""
        data = super()._init_data(label=label)
        return cls(data=data)

    def to_numpy(self):
        """todo"""
        try:
            return numpy.array(self.to_sympy(), dtype=complex)[:, 0]
        except TypeError:
            return numpy.array(self.to_sympy(), dtype=object)[:, 0]

    def norm(self):
        """todo"""
        return sympy.sqrt(self.inner(self)).simplify()

    def is_unit_norm(self):
        """todo"""
        try:
            norm = numpy.linalg.norm(self.to_numpy())
            return numpy.allclose(norm, 1)
        except TypeError:
            return self.norm() == 1

    def is_valid(self):
        """todo"""
        return self.is_unit_norm()

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
        return (self.to_sympy().T @ other.to_sympy())[0]

    def outer(self, other):
        """todo"""
        if not isinstance(other, Statevector):
            other = Statevector(other)
        if len(self) != len(other):
            raise ValueError
        return self.to_sympy() @ other.to_sympy().T

    def projector(self):
        """todo"""
        return self.outer(self)
