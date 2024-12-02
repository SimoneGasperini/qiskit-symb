r"""Symbolic Pauli :math:`Y` and controlled-:math:`Y` gates module"""

from sympy import I
from sympy.tensor.array import Array
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class YGate(StandardGate):
    r"""Symbolic Pauli math:`Y` gate class"""
    gate_name = 'Y'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[0, -1j],
                      [1j, 0]])


class CYGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`Y` gate class"""
    gate_name = 'CY'
    gate_name_latex = r'\text{CY}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = YGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = YGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
