r"""Symbolic :math:`P(\lambda)` and controlled-:math:`P(\lambda)` gates module"""

from sympy import exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class PhaseGate(ParametricGate):
    r"""Symbolic :math:`P(\lambda)` gate class"""
    gate_name = 'P'

    def __init__(self, lam, qubit):
        """todo"""
        params = (lam,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        lam, = self.params
        explam = exp(1j * lam)
        return Array([[1, 0],
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
