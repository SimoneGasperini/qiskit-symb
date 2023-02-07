r"""Symbolic Pauli :math:`Z` gate module"""

from qiskit.circuit.library import ZGate
from qiskit_symbolic.gate import GateSymb


class ZGateSymb(ZGate, GateSymb):
    r"""Symbolic Pauli :math:`Z` gate class"""

    def __init__(self, label=None):
        """todo"""
        super().__init__(label=label)
