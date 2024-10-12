r"""Symbolic :math:`P(\lambda)` and controlled-:math:`P(\lambda)` gates module"""

from sympy import Matrix, I, exp
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class PhaseGate(ParametricGate):
    r"""Symbolic :math:`P(\lambda)` gate class"""
    gate_name = 'P'
    gate_name_latex = r'\text{P}'

    def __new__(cls, theta, target):
        """todo"""
        qubits = (target,)
        params = (theta,)
        return super().__new__(cls, qubits=qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        lam, = self.get_params_expr()
        sympy_matrix = Matrix([[1, 0],
                               [0, exp(I*lam)]])
        return sympy_matrix


class CPhaseGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`P(\lambda)` gate class"""
    gate_name = 'CP'
    gate_name_latex = r'\text{CP}'

    def __new__(cls, theta, control, target):
        """todo"""
        controls = (control,)
        target_gate = PhaseGate(theta=theta, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)
