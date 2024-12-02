r"""Symbolic Pauli :math:`X` and controlled-:math:`X` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class XGate(StandardGate):
    r"""Symbolic Pauli math:`X` gate class"""
    gate_name = 'X'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[0, 1],
                      [1, 0]])


class CXGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`X` gate class"""
    gate_name = 'CX'
    gate_name_latex = r'\text{CX}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = XGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = XGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
