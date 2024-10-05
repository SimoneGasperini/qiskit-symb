r"""Symbolic :math:`RZX(\theta)` and controlled-:math:`RZX(\theta)` gates module"""

from sympy import Matrix, I, sin, cos
from ...gate import ParametricGate
from ...controlledgate import ControlledGate


class RZXGate(ParametricGate):
    r"""Symbolic :math:`RZX(\theta)` gate class"""
    gate_name = 'RZX'
    gate_name_latex = 'RZX'

    def __new__(cls, theta, *qubits):
        """todo"""
        params = (theta,)
        return super().__new__(cls, *qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, = self.get_params_expr()
        sympy_matrix = Matrix([[cos(theta/2), 0, -I*sin(theta/2), 0],
                               [0, cos(theta/2), 0, I*sin(theta/2)],
                               [-I*sin(theta/2), 0, cos(theta/2), 0],
                               [0, I*sin(theta/2), 0, cos(theta/2)]])
        return sympy_matrix


class CRZXGate(ControlledGate):
    r"""Symbolic controlled-:math:`RZX` gate class"""

    def __init__(self, theta, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = RZXGate(theta=theta)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='crzx', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
