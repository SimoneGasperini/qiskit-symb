r"""Symbolic Hadamard :math:`H` and controlled-:math:`H` gates module"""

from sympy import Matrix, Pow, Rational
from sympy.physics.quantum.gate import H
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class HGate(StandardGate, H):
    r"""Symbolic math:`H` gate class"""
    gate_name = 'H'
    gate_name_latex = r'\text{H}'

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)

    def __init__(self, target):
        """todo"""
        self.params = ()
        self.qubits = (target,)

    @staticmethod
    def _sympy_matrix():
        sqrt2_inv = Pow(2, Rational(-1, 2), evaluate=False)
        return sqrt2_inv * Matrix([[1, 1],
                                   [1, -1]])


class CHGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`H` gate class"""
    gate_name = 'CH'
    gate_name_latex = r'\text{CH}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = HGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = HGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
