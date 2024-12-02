r"""Symbolic :math:`R(\theta, \phi)` and controlled-:math:`R(\theta, \phi)` gates module"""

from sympy import sin, cos, exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class RGate(ParametricGate):
    r"""Symbolic :math:`R(\theta, \phi)` gate class"""
    gate_name = 'R'

    def __init__(self, theta, phi, qubit):
        """todo"""
        params = (theta, phi)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, phi = self.params
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        plusexp = 1j * exp(1j * phi)
        minusexp = 1j * exp(-1j * phi)
        return Array([[costh2, -minusexp*sinth2],
                      [-plusexp*sinth2, costh2]])


class CRGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`R` gate class"""
    gate_name = 'CR'
    gate_name_latex = r'\text{CR}'

    def __new__(cls, theta, phi, control, target):
        """todo"""
        controls = (control,)
        target_gate = RGate(theta=theta, phi=phi, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, theta, phi, control, target):
        """todo"""
        target_gate = RGate(theta=theta, phi=phi, target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
