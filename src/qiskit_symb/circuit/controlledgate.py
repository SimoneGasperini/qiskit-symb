"""Symbolic controlled gate module"""

from sympy.physics.quantum.gate import CGate
from .gate import Gate


class ControlledGate(Gate, CGate):
    """Symbolic controlled gate abstract class"""

    def __new__(cls, controls, target_gate):
        """todo"""
        return CGate.__new__(cls, *controls, target_gate)

    def get_target_matrix(self, format='sympy'):
        """todo"""
        return self.gate._sympy_matrix()
