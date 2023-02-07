r"""Symbolic :math:`RX(\theta)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit.circuit.library import RXGate
from qiskit_symbolic.gate import GateSymb


class RXGateSymb(RXGate, GateSymb):
    r"""Symbolic :math:`RX(\theta)` gate class"""

    def __init__(self, theta, qubits=None, label=None):
        """todo"""
        super().__init__(theta=theta, label=label)
        self.qubits = qubits

    def __sympy__(self):
        """todo"""
        theta, = self.get_sympy_params()
        i = sympy.I
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        return Matrix([[cos, -i * sin],
                       [-i * sin, cos]])
