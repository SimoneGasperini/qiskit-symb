r"""Symbolic :math:`RX(\theta)` and controlled-:math:`RX(\theta)` gates module"""

from sympy import Matrix, I, sin, cos
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class RXGate(ParametricGate):
    r"""Symbolic :math:`RX(\theta)` gate class"""
    gate_name = 'RX'
    gate_name_latex = r'\text{RX}'

    def __new__(cls, theta, target):
        """todo"""
        params = (theta,)
        qubits = (target,)
        return super().__new__(cls, params=params, qubits=qubits)

    def __init__(self, theta, target):
        """todo"""
        self.params = (theta,)
        self.qubits = (target,)

    def _sympy_matrix(self):
        """todo"""
        theta, = self.get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        return Matrix([[costh2, -I*sinth2],
                       [-I*sinth2, costh2]])


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
