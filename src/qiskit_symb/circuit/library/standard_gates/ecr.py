r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate


class ECRGate(Gate):
    r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='ecr', num_qubits=2, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return 1/sympy.sqrt(2) * Matrix([[0, 1, 0, i],
                                         [1, 0, -i, 0],
                                         [0, i, 0, 1],
                                         [-i, 0, 1, 0]])
