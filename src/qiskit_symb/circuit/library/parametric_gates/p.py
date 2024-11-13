r"""Symbolic :math:`P(\lambda)` and controlled-:math:`P(\lambda)` gates module"""

from sympy import Matrix, I, exp
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class PhaseGate(ParametricGate):
    r"""Symbolic :math:`P(\lambda)` gate class"""
    gate_name = 'P'
    gate_name_latex = r'\text{P}'

    def __new__(cls, lam, target):
        """todo"""
        params = (lam,)
        qubits = (target,)
        return super().__new__(cls, params=params, qubits=qubits)

    def __init__(self, lam, target):
        """todo"""
        self.params = (lam,)
        self.qubits = (target,)

    def _sympy_matrix(self):
        """todo"""
        lam, = self.get_params_expr()
        explam = exp(I * lam)
        return Matrix([[1, 0],
                       [0, explam]])


class CPhaseGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`P(\lambda)` gate class"""
    gate_name = 'CP'
    gate_name_latex = r'\text{CP}'

    def __new__(cls, lam, control, target):
        """todo"""
        controls = (control,)
        target_gate = PhaseGate(lam=lam, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, lam, control, target):
        """todo"""
        target_gate = PhaseGate(lam=lam, target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
