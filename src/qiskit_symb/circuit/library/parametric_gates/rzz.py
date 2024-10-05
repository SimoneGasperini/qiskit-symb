r"""Symbolic :math:`RZZ(\theta)` and controlled-:math:`RZZ(\theta)` gates module"""

from sympy import Matrix, I, exp
from ...gate import ParametricGate
from ...controlledgate import ControlledGate


class RZZGate(ParametricGate):
    r"""Symbolic :math:`RZZ(\theta)` gate class"""
    gate_name = 'RZZ'
    gate_name_latex = 'RZZ'

    def __new__(cls, theta, *qubits):
        """todo"""
        params = (theta,)
        return super().__new__(cls, *qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, = self.get_params_expr()
        sympy_matrix = Matrix([[exp(-I*theta/2), 0, 0, 0],
                               [0, exp(I*theta/2), 0, 0],
                               [0, 0, exp(I*theta/2), 0],
                               [0, 0, 0, exp(-I*theta/2)]])
        return sympy_matrix


class CRZZGate(ControlledGate):
    r"""Symbolic controlled-:math:`RZZ` gate class"""

    def __init__(self, theta, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = RZZGate(theta=theta)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='crzz', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
