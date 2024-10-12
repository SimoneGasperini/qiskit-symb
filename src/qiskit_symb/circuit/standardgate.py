"""Symbolic standard gate module"""

from sympy import matrix2numpy
from .gate import Gate


class StandardGate(Gate):
    """Symbolic standard gate abstract class"""

    def get_numpy_repr(self, nqubits):
        """todo"""
        matrix = self.get_sympy_repr(nqubits=nqubits)
        numpy_matrix = matrix2numpy(matrix, dtype=complex)
        return numpy_matrix
