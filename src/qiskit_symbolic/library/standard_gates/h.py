r"""Symbolic Hadamard :math:`H` gate module"""

from qiskit.circuit.library import HGate
from qiskit_symbolic.gate import GateSymb


class HGateSymb(HGate, GateSymb):
    r"""Symbolic Hadamard :math:`H` gate class"""

    def __init__(self, label=None):
        """todo"""
        super().__init__(label=label)
