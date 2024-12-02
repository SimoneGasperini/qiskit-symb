"""Symbolic standard gate module"""

from sympy import Matrix, matrix2numpy
from .gate import Gate


class StandardGate(Gate):
    """Symbolic standard gate abstract class"""

    def get_numpy_repr(self):
        """todo"""
        sympy_matrix = Matrix(self.to_sympy())
        numpy_matrix = matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix
