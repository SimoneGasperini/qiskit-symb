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
        params = (theta, phi)
        qubits = (target,)
        return super().__new__(cls, params=params, qubits=qubits)

    def __init__(self, theta, phi, target):
        """todo"""
        self.params = (theta, phi)
        self.qubits = (target,)

    def _sympy_matrix(self):
        """todo"""
        theta, phi = self.get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        plusexp = I * exp(I * phi)
        minusexp = I * exp(-I * phi)
        return Matrix([[costh2, -minusexp*sinth2],
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
