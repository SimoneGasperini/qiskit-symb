r"""Symbolic :math:`RZZ(\theta)` and controlled-:math:`RZZ(\theta)` gates module"""

from sympy import exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class RZZGate(ParametricGate):
    r"""Symbolic :math:`RZZ(\theta)` gate class"""

    def __init__(self, theta, qubit1, qubit2):
        """todo"""
        params = (theta,)
        qubits = (qubit1, qubit2)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, = self._get_params_expr()
        plusexp = exp(1j * theta/2)
        minusexp = exp(-1j * theta/2)
        return Array([[minusexp, 0, 0, 0],
                      [0, plusexp, 0, 0],
                      [0, 0, plusexp, 0],
                      [0, 0, 0, minusexp]])
