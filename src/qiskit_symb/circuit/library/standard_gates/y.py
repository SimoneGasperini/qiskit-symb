r"""Symbolic Pauli :math:`Y` and controlled-:math:`Y` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class YGate(StandardGate):
    r"""Symbolic Pauli math:`Y` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[0, -1j],
                      [1j, 0]])


class CYGate(StandardGate):
    r"""Symbolic controlled-:math:`Y` gate class"""

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
                      [0, 0, 0, -1j],
                      [0, 0, 1j, 0]])
