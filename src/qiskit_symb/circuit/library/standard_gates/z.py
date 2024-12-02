r"""Symbolic Pauli :math:`Z` and controlled-:math:`Z` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class ZGate(StandardGate):
    r"""Symbolic Pauli math:`Z` gate class"""
    gate_name = 'Z'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, -1]])


class CZGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`Z` gate class"""
    gate_name = 'CZ'
    gate_name_latex = r'\text{CZ}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = ZGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = ZGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
