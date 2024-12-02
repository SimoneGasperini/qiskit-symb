r"""Symbolic :math:`RYY(\theta)` and controlled-:math:`RYY(\theta)` gates module"""

from sympy import sin, cos
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class RYYGate(ParametricGate):
    r"""Symbolic :math:`RYY(\theta)` gate class"""

    def __init__(self, theta, qubit1, qubit2):
        """todo"""
        params = (theta,)
        qubits = (qubit1, qubit2)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, = self._get_params_expr()
        costh2 = cos(theta / 2)
        isinth2 = 1j * sin(theta / 2)
        return Array([[costh2, 0, 0, isinth2],
                      [0, costh2, -isinth2, 0],
                      [0, -isinth2, costh2, 0],
                      [isinth2, 0, 0, costh2]])
