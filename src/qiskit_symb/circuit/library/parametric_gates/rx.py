r"""Symbolic :math:`RX(\theta)` and controlled-:math:`RX(\theta)` gates module"""

from sympy import sin, cos
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class RXGate(ParametricGate):
    r"""Symbolic :math:`RX(\theta)` gate class"""
    gate_name = 'RX'

    def __init__(self, theta, qubit):
        """todo"""
        params = (theta,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, = self.params
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        return Array([[costh2, -1j*sinth2],
                      [-1j*sinth2, costh2]])


class CRXGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`RX(\theta)` gate class"""
    gate_name = 'CRX'
    gate_name_latex = r'\text{CRX}'

    def __new__(cls, theta, control, target):
        """todo"""
        controls = (control,)
        target_gate = RXGate(theta=theta, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, theta, control, target):
        """todo"""
        target_gate = RXGate(theta=theta, target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
