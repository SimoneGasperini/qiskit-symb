"""Symbolic parametric gate module"""

from sympy import Symbol, matrix2numpy
from sympy.physics.quantum import represent
from .gate import Gate


class ParametricGate(Gate):
    """Symbolic parametric gate abstract class"""

    def get_numpy_repr(self, nqubits, par2val):
        """todo"""
        sympy_matrix = represent(self, nqubits=nqubits)
        symb2val = {Symbol(par.name): val for par, val in par2val.items()}
        numpy_matrix = matrix2numpy(sympy_matrix.subs(symb2val), dtype=complex)
        return numpy_matrix
