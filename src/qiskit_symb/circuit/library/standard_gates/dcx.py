r"""Symbolic Double-CNOT :math:`DCX` gate module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate


class DCXGate(Gate):
    r"""Symbolic Double-CNOT :math:`DCX` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='dcx', sympy_name='DCX', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = Matrix([[1, 0, 0, 0],
                               [0, 0, 0, 1],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0]])
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix
