r"""Symbolic Pauli :math:`Z` and controlled-:math:`Z` gates module"""

from sympy import Matrix
from sympy.physics.quantum.gate import Z
from ...gate import StandardGate, ControlledGate


class ZGate(StandardGate, Z):
    r"""Symbolic Pauli math:`Z` gate class"""
    gate_name = 'Z'
    gate_name_latex = r'\text{Z}'
    sympy_matrix = Matrix([[1, 0],
                           [0, -1]])

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)


class CZGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`Z` gate class"""
    gate_name = 'CZ'
    gate_name_latex = r'\text{CZ}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = ZGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)
