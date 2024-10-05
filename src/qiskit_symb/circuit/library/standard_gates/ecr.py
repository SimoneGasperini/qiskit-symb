r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate module"""

from sympy import Matrix, I, sqrt
from ...gate import StandardGate


class ECRGate(StandardGate):
    r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate class"""
    gate_name = 'ECR'
    gate_name_latex = 'ECR'
    sympy_matrix = 1/sqrt(2) * Matrix([[0, 1, 0, I],
                                       [1, 0, -I, 0],
                                       [0, I, 0, 1],
                                       [-I, 0, 1, 0]])
