r"""Symbolic Hadamard :math:`H` and controlled-:math:`H` gates module"""

from sympy import Matrix, sqrt
from sympy.physics.quantum.gate import H
from ...gate import StandardGate, ControlledGate


class HGate(StandardGate, H):
    r"""Symbolic math:`H` gate class"""
    gate_name = 'H'
    gate_name_latex = r'\text{H}'
    sympy_matrix = 1/sqrt(2) * Matrix([[1, 1],
                                       [1, -1]])

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)


class CHGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`H` gate class"""
    gate_name = 'CH'
    gate_name_latex = r'\text{CH}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = HGate(target=target)
        return ControlledGate.__new__(cls, controls=controls, target_gate=target_gate)
