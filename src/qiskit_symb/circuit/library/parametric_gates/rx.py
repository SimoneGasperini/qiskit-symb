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
        qubits = (target,)
        params = (theta,)
        return super().__new__(cls, qubits=qubits, params=params)

    def _sympy_matrix(self):
        """todo"""
        theta, = self.get_params_expr()
        return Matrix([[cos(theta/2), -I*sin(theta/2)],
                       [-I*sin(theta/2), cos(theta/2)]])


class CRXGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`RX(\theta)` gate class"""
    gate_name = 'CRX'
    gate_name_latex = r'\text{CRX}'

    def __new__(cls, theta, control, target):
        """todo"""
        controls = (control,)
        target_gate = RXGate(theta=theta, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)
