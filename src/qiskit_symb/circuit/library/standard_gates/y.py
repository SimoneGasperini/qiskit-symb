r"""Symbolic Pauli :math:`Y` and controlled-:math:`Y` gates module"""

from sympy import Matrix, I
from sympy.physics.quantum.gate import Y
from ...gate import StandardGate, ControlledGate


class YGate(StandardGate, Y):
    r"""Symbolic Pauli math:`Y` gate class"""
    gate_name = 'Y'
    gate_name_latex = r'\text{Y}'
    sympy_matrix = Matrix([[0, -I],
                           [I, 0]])

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)


class CYGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`Y` gate class"""
    gate_name = 'CY'
    gate_name_latex = r'\text{CY}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = YGate(target=target)
        return ControlledGate.__new__(cls, controls=controls, target_gate=target_gate)
