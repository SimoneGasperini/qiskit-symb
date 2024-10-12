r"""Symbolic :math:`RY(\theta)` and controlled-:math:`RY(\theta)` gates module"""

from sympy import Matrix, sin, cos
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class RYGate(ParametricGate):
    r"""Symbolic :math:`RY(\theta)` gate class"""
    gate_name = 'RY'
    gate_name_latex = r'\text{RY}'

    def __new__(cls, theta, target):
        """todo"""
        qubits = (target,)
        params = (theta,)
        return super().__new__(cls, qubits=qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, = self.get_params_expr()
        return Matrix([[cos(theta/2), -sin(theta/2)],
                       [sin(theta/2), cos(theta/2)]])


class CRYGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`RY(\theta)` gate class"""
    gate_name = 'CRY'
    gate_name_latex = r'\text{CRY}'

    def __new__(cls, theta, control, target):
        """todo"""
        controls = (control,)
        target_gate = RYGate(theta=theta, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)
