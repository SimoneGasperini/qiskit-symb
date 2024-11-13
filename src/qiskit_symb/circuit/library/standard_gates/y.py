r"""Symbolic Pauli :math:`Y` and controlled-:math:`Y` gates module"""

from sympy import Matrix, I
from sympy.physics.quantum.gate import Y
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class YGate(StandardGate, Y):
    r"""Symbolic Pauli math:`Y` gate class"""
    gate_name = 'Y'
    gate_name_latex = r'\text{Y}'

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
        return Matrix([[0, -I],
                       [I, 0]])


class CYGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`Y` gate class"""
    gate_name = 'CY'
    gate_name_latex = r'\text{CY}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = YGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = YGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
