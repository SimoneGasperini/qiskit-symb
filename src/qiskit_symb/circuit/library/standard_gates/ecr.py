r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate


class ECRGate(Gate):
    r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='ecr', sympy_name='ECR', params=())

    def __sympy__(self):
        """todo"""
        i = sympy.I
        sympy_matrix = 1/sympy.sqrt(2) * Matrix([[0, 1, 0, i],
                                                 [1, 0, -i, 0],
                                                 [0, i, 0, 1],
                                                 [-i, 0, 1, 0]])
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix
