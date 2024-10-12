"""Symbolic controlled gate module"""

from sympy.physics.quantum.gate import CGate
from .gate import Gate


class ControlledGate(Gate, CGate):
    """Symbolic controlled gate abstract class"""
    def __new__(cls, controls, target_gate):
        return CGate.__new__(cls, *controls, target_gate)

    @property
    def qubits_label(self):
        """todo"""
        return ','.join(str(s) for s in self.controls + self.targets)

    @property
    def params(self):
        """todo"""
        return self.gate.params

    def get_target_matrix(self, format='sympy'):
        """todo"""
        return self.gate.sympy_matrix
