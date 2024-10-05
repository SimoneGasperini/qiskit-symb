r"""Symbolic :math:`P(\lambda)` and controlled-:math:`P(\lambda)` gates module"""

from sympy import Matrix, I, exp
from ...gate import ParametricGate
from ...controlledgate import ControlledGate


class PhaseGate(ParametricGate):
    r"""Symbolic :math:`P(\lambda)` gate class"""
    gate_name = 'P'
    gate_name_latex = 'P'

    def __new__(cls, theta, *qubits):
        """todo"""
        params = (theta,)
        return super().__new__(cls, *qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        lam, = self.get_params_expr()
        sympy_matrix = Matrix([[1, 0],
                               [0, exp(I*lam)]])
        return sympy_matrix


class CPhaseGate(ControlledGate):
    r"""Symbolic controlled-:math:`P(\lambda)` gate class"""

    def __init__(self, theta, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = PhaseGate(theta=theta)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cp', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
