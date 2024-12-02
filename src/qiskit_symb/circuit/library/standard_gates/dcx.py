r"""Symbolic Double-CNOT :math:`DCX` gate module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class DCXGate(StandardGate):
    r"""Symbolic Double-CNOT :math:`DCX` gate class"""

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
                      [0, 0, 0, 1],
                      [0, 1, 0, 0]])
