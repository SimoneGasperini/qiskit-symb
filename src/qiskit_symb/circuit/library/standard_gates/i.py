r"""Symbolic Pauli :math:`I` gate module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class IGate(StandardGate):
    r"""Symbolic Pauli math:`I` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, 1]])
