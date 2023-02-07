r"""Symbolic :math:`RY(\theta)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit.circuit.library import RYGate
from qiskit_symbolic.gate import GateSymb


class RYGateSymb(RYGate, GateSymb):
    r"""Symbolic :math:`RY(\theta)` gate class"""

    def __init__(self, theta, qubits=None, label=None):
        """todo"""
        super().__init__(theta=theta, label=label)
        self.qubits = qubits

    def __sympy__(self):
        """todo"""
        theta, = self.get_sympy_params()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        return Matrix([[cos, -sin],
                       [sin, cos]])
