"""Symbolic standard gate module"""

from sympy import matrix2numpy
from sympy.physics.quantum import represent
from .gate import Gate


class StandardGate(Gate):
    """Symbolic standard gate abstract class"""

    def get_numpy_repr(self, nqubits):
        """todo"""
        sympy_matrix = represent(self, nqubits=nqubits)
        numpy_matrix = matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix
