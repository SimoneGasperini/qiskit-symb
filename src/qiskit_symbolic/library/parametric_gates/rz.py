r"""Symbolic :math:`RZ(\lambda)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit.circuit.library import RZGate
from qiskit_symbolic.gate import GateSymb


class RZGateSymb(RZGate, GateSymb):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""

    def __init__(self, phi, label=None):
        """todo"""
        super().__init__(phi=phi, label=label)

    def __sympy__(self):
        """todo"""
        lam, = self.get_sympy_params()
        i = sympy.I
        return Matrix([[sympy.exp(-i * lam/2), 0],
                       [0, sympy.exp(i * lam/2)]])
