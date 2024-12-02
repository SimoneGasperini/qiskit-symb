"""Symbolic parametric gate module"""

from sympy import Symbol, Matrix, matrix2numpy
from .gate import Gate


class ParametricGate(Gate):
    """Symbolic parametric gate abstract class"""

    def get_numpy_repr(self, par2val):
        """todo"""
        sympy_matrix = Matrix(self.to_sympy())
        symb2val = {Symbol(par.name): val for par, val in par2val.items()}
        numpy_matrix = matrix2numpy(sympy_matrix.subs(symb2val), dtype=complex)
        return numpy_matrix
