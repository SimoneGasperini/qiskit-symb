r"""Symbolic Pauli :math:`I` gate module"""

import sympy
from sympy.physics.quantum.gate import IdentityGate
from ...gate import Gate


class IGate(Gate, IdentityGate):
    r"""Symbolic Pauli :math:`I` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='id', sympy_name='I', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = self.get_target_matrix()
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix
