r"""Symbolic :math:`iSWAP` and controlled-:math:`iSWAP` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class iSwapGate(StandardGate):
    r"""Symbolic :math:`iSWAP` gate class"""

    def __init__(self, qubit1, qubit2):
        """todo"""
        params = ()
        qubits = (qubit1, qubit2)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0, 0, 0],
                      [0, 0, 1j, 0],
                      [0, 1j, 0, 0],
                      [0, 0, 0, 1]])
