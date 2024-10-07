r"""Symbolic Pauli :math:`X` and controlled-:math:`X` gates module"""

from sympy import Matrix
from sympy.physics.quantum.gate import X
from ...gate import StandardGate, ControlledGate


class XGate(StandardGate, X):
    r"""Symbolic Pauli math:`X` gate class"""
    gate_name = 'X'
    gate_name_latex = r'\text{X}'
    sympy_matrix = Matrix([[0, 1],
                           [1, 0]])

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)


class CXGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`X` gate class"""
    gate_name = 'CX'
    gate_name_latex = r'\text{CX}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = XGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)
