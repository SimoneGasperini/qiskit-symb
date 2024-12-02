r"""Symbolic Pauli :math:`Z` and controlled-:math:`Z` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class ZGate(StandardGate):
    r"""Symbolic Pauli math:`Z` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, -1]])


class CZGate(StandardGate):
    r"""Symbolic controlled-:math:`Z` gate class"""

    def __init__(self, control, target):
        """todo"""
        params = ()
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, -1]])
