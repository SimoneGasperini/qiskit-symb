r"""Symbolic :math:`U(\theta, \phi, \lambda)` and
controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gates module"""

from sympy import Matrix, I, sin, cos, exp
from ...gate import ParametricGate
from ...controlledgate import ControlledGate


class UGate(ParametricGate):
    r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate class"""
    gate_name = 'U'
    gate_name_latex = 'U'

    def __new__(cls, theta, phi, lam, _gamma=0, *qubits):
        """todo"""
        params = (theta, phi, lam, _gamma)
        return super().__new__(cls, *qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, phi, lam, gamma = self.get_params_expr()
        sympy_matrix = exp(I * gamma) * Matrix([[cos(theta/2), -exp(I*lam)*sin(theta/2)],
                                                [exp(I*phi)*sin(theta/2), exp(I*(phi+lam))*cos(theta/2)]])
        return sympy_matrix


class CUGate(ControlledGate):
    r"""Symbolic controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gate class"""

    def __init__(self, theta, phi, lam, gamma=0, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = UGate(theta=theta, phi=phi, lam=lam, _gamma=gamma)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cu', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
