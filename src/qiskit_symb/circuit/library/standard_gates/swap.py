r"""Symbolic :math:`SWAP` and controlled-:math:`SWAP` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class SwapGate(StandardGate):
    r"""Symbolic :math:`SWAP` gate class"""

    def __init__(self, qubit1, qubit2):
        """todo"""
        params = ()
        qubits = (qubit1, qubit2)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]])
