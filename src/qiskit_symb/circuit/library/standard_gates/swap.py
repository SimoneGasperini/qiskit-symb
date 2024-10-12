r"""Symbolic :math:`SWAP` and controlled-:math:`SWAP` gates module"""

from sympy import Matrix
from sympy.physics.quantum.gate import SWAP
from ...standardgate import StandardGate


class SwapGate(StandardGate, SWAP):
    r"""Symbolic :math:`SWAP` gate class"""
    gate_name = 'SWAP'
    gate_name_latex = r'\text{SWAP}'
    sympy_matrix = Matrix([[1, 0, 0, 0],
                           [0, 0, 1, 0],
                           [0, 1, 0, 0],
                           [0, 0, 0, 1]])

    def __new__(cls, targets):
        """todo"""
        qubits = targets
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)
