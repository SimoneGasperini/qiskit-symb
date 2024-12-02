r"""Symbolic :math:`RX(\theta)` and controlled-:math:`RX(\theta)` gates module"""

from sympy import sin, cos
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class RXGate(ParametricGate):
    r"""Symbolic :math:`RX(\theta)` gate class"""

    def __init__(self, theta, qubit):
        """todo"""
        params = (theta,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, = self._get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        return Array([[costh2, -1j*sinth2],
                      [-1j*sinth2, costh2]])


class CRXGate(ParametricGate):
    r"""Symbolic controlled-:math:`RX(\theta)` gate class"""

    def __init__(self, theta, control, target):
        """todo"""
        params = (theta,)
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, = self._get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, costh2, -1j*sinth2],
                      [0, 0, -1j*sinth2, costh2]])
