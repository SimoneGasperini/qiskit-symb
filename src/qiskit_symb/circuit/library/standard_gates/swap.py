r"""Symbolic :math:`SWAP` and controlled-:math:`SWAP` gates module"""

from sympy import Matrix
from sympy.physics.quantum.gate import SWAP
from ...standardgate import StandardGate


class SwapGate(StandardGate, SWAP):
    r"""Symbolic :math:`SWAP` gate class"""
    gate_name = 'SWAP'
    gate_name_latex = r'\text{SWAP}'

    def __new__(cls, target1, target2):
        """todo"""
        qubits = (target1, target2)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)

    @staticmethod
    def _sympy_matrix():
        return Matrix([[1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]])
