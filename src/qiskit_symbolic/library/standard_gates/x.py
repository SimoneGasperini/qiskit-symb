r"""Symbolic :math:`X` and :math:`CX` gates module"""

from qiskit.circuit.library import XGate, CXGate
from qiskit_symbolic.gate import GateSymb


class XGateSymb(XGate, GateSymb):
    r"""Symbolic Pauli :math:`X` gate class"""

    def __init__(self, label=None):
        """todo"""
        super().__init__(label=label)


class CXGateSymb(CXGate, GateSymb):
    r"""Symbolic controlled-not :math:`CX` gate class"""

    def __init__(self, ctrl_qubit, tg_qubit, label=None):
        """todo"""
        super().__init__(label=label)
        self.ctrl_qubit = ctrl_qubit
        self.tg_qubit = tg_qubit
        self.base_gate = GateSymb.from_instruction(self.base_gate)
