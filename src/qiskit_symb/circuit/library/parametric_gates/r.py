r"""Symbolic :math:`R(\theta, \phi)` and controlled-:math:`R(\theta, \phi)` gates module"""

from sympy import Matrix, I, sin, cos, exp
from ...gate import ParametricGate
from ...controlledgate import ControlledGate


class RGate(ParametricGate):
    r"""Symbolic :math:`R(\theta, \phi)` gate class"""
    gate_name = 'R'
    gate_name_latex = 'R'

    def __new__(cls, theta, phi, *qubits):
        """todo"""
        params = (theta, phi)
        return super().__new__(cls, *qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, phi = self.get_params_expr()
        sympy_matrix = Matrix([[cos(theta/2), -I*exp(-I*phi)*sin(theta/2)],
                               [-I*exp(I*phi)*sin(theta/2), cos(theta/2)]])
        return sympy_matrix


class CRGate(ControlledGate):
    r"""Symbolic controlled-:math:`R` gate class"""

    def __init__(self, theta, phi, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = RGate(theta=theta, phi=phi)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cr', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
