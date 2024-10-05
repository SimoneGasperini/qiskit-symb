r"""Symbolic Double-CNOT :math:`DCX` gate module"""

from sympy import Matrix
from ...gate import StandardGate


class DCXGate(StandardGate):
    r"""Symbolic Double-CNOT :math:`DCX` gate class"""
    gate_name = 'DCX'
    gate_name_latex = 'DCX'
    sympy_matrix = Matrix([[1, 0, 0, 0],
                           [0, 0, 0, 1],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0]])
