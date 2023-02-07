r"""Symbolic Pauli :math:`Y` gate module"""

from qiskit.circuit.library import YGate
from qiskit_symbolic.gate import GateSymb


class YGateSymb(YGate, GateSymb):
    r"""Symbolic Pauli :math:`Y` gate class"""

    def __init__(self, qubits=None, label=None):
        """todo"""
        super().__init__(label=label)
        self.qubits = qubits
