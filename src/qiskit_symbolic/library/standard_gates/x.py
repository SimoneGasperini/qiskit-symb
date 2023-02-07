r"""Symbolic :math:`X` and :math:`CX` gates module"""

from qiskit.circuit.library import XGate, CXGate
from qiskit_symbolic.gate import GateSymb


class XGateSymb(XGate, GateSymb):
    r"""Symbolic Pauli :math:`X` gate class"""

    def __init__(self, qubits=None, label=None):
        """todo"""
        super().__init__(label=label)
        self.qubits = qubits


class CXGateSymb(CXGate, GateSymb):
    r"""Symbolic controlled-not :math:`CX` gate class"""

    def __init__(self, qubits=None, label=None):
        """todo"""
        super().__init__(label=label)
        self.qubits = qubits
