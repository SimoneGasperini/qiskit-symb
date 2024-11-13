r"""Symbolic Pauli :math:`Z` and controlled-:math:`Z` gates module"""

from sympy import Matrix
from sympy.physics.quantum.gate import Z
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class ZGate(StandardGate, Z):
    r"""Symbolic Pauli math:`Z` gate class"""
    gate_name = 'Z'
    gate_name_latex = r'\text{Z}'

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)

    def __init__(self, target):
        """todo"""
        self.params = ()
        self.qubits = (target,)

    @staticmethod
    def _sympy_matrix():
        return Matrix([[1, 0],
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
