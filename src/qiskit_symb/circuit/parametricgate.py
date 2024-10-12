"""Symbolic parametric gate module"""

from sympy import Symbol, matrix2numpy
from .gate import Gate


class ParametricGate(Gate):
    """Symbolic parametric gate abstract class"""

    def get_numpy_repr(self, nqubits, par2val):
        """todo"""
        symb2val = {Symbol(par.name): val for par, val in par2val.items()}
        matrix = self.get_sympy_repr(nqubits=nqubits).subs(symb2val)
        numpy_matrix = matrix2numpy(matrix, dtype=complex)
        return numpy_matrix
