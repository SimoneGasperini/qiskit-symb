r"""Symbolic Pauli :math:`X` and controlled-:math:`X` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class XGate(StandardGate):
    r"""Symbolic Pauli math:`X` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[0, 1],
                      [1, 0]])


class CXGate(StandardGate):
    r"""Symbolic controlled-:math:`X` gate class"""

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
                      [0, 0, 0, 1],
                      [0, 0, 1, 0]])
