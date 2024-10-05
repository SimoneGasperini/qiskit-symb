r"""Symbolic Pauli :math:`I` gate module"""

from sympy import Matrix
from sympy.physics.quantum.gate import IdentityGate
from ...gate import StandardGate


class IGate(StandardGate, IdentityGate):
    r"""Symbolic Pauli math:`I` gate class"""
    gate_name = 'I'
    gate_name_latex = 'I'
    sympy_matrix = Matrix([[1, 0],
                           [0, 1]])
