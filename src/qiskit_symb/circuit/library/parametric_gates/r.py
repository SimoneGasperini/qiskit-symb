r"""Symbolic :math:`R(\theta, \phi)` and controlled-:math:`R(\theta, \phi)` gates module"""

from sympy import sin, cos, exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class RGate(ParametricGate):
    r"""Symbolic :math:`R(\theta, \phi)` gate class"""

    def __init__(self, theta, phi, qubit):
        """todo"""
        params = (theta, phi)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, phi = self._get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        plusexp = 1j * exp(1j * phi)
        minusexp = 1j * exp(-1j * phi)
        return Array([[costh2, -minusexp*sinth2],
                      [-plusexp*sinth2, costh2]])


class CRGate(ParametricGate):
    r"""Symbolic controlled-:math:`R(\theta, \phi)` gate class"""

    def __init__(self, theta, phi, control, target):
        """todo"""
        params = (theta, phi)
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, phi = self._get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        plusexp = 1j * exp(1j * phi)
        minusexp = 1j * exp(-1j * phi)
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, costh2, -minusexp*sinth2],
                      [0, 0, -plusexp*sinth2, costh2]])
