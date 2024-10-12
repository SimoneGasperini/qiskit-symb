r"""Symbolic :math:`R(\theta, \phi)` and controlled-:math:`R(\theta, \phi)` gates module"""

from sympy import Matrix, I, sin, cos, exp
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class RGate(ParametricGate):
    r"""Symbolic :math:`R(\theta, \phi)` gate class"""
    gate_name = 'R'
    gate_name_latex = r'\text{P}'

    def __new__(cls, theta, phi, target):
        """todo"""
        qubits = (target,)
        params = (theta, phi)
        return super().__new__(cls, qubits=qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, phi = self.get_params_expr()
        return Matrix([[cos(theta/2), -I*exp(-I*phi)*sin(theta/2)],
                       [-I*exp(I*phi)*sin(theta/2), cos(theta/2)]])


class CRGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`R` gate class"""
    gate_name = 'CR'
    gate_name_latex = r'\text{CR}'

    def __new__(cls, theta, phi, control, target):
        """todo"""
        controls = (control,)
        target_gate = RGate(theta=theta, phi=phi, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)
