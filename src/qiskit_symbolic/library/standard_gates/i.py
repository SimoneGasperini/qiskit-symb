r"""Symbolic Pauli :math:`I` gate module"""

from qiskit.circuit.library import IGate
from qiskit_symbolic.gate import GateSymb


class IGateSymb(IGate, GateSymb):
    r"""Symbolic Pauli :math:`I` gate class"""

    def __init__(self, label=None):
        """todo"""
        super().__init__(label=label)
