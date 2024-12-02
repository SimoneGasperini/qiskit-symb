r"""Symbolic Hadamard :math:`H` and controlled-:math:`H` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class HGate(StandardGate):
    r"""Symbolic math:`H` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        x = 1 / 2**0.5
        return Array([[x, x],
                      [x, -x]])


class CHGate(StandardGate):
    r"""Symbolic controlled-:math:`H` gate class"""

    def __init__(self, control, target):
        """todo"""
        params = ()
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        x = 1 / 2**0.5
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, x, x],
                      [0, 0, x, -x]])
