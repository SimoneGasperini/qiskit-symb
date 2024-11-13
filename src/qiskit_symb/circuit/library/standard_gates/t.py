r"""Symbolic :math:`T`, :math:`T^{\dagger}`, controlled-:math:`T`,
and controlled-:math:`T^{\dagger}` gates module"""

from sympy import Matrix, I, pi, exp
from sympy.physics.quantum.gate import T
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class TGate(StandardGate, T):
    r"""Symbolic :math:`T` gate class"""
    gate_name = 'T'
    gate_name_latex = r'\text{T}'

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
                       [0, exp(I*pi/4)]])


class TdgGate(StandardGate):
    r"""Symbolic :math:`T^{\dagger}` gate class"""
    gate_name = 'T^\\dagger'
    gate_name_latex = r'\text{T}^\dagger'

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
        return TGate._sympy_matrix().H


class CTGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`T` gate class"""
    gate_name = 'CT'
    gate_name_latex = r'\text{CT}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = TGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = TGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)


class CTdgGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`T^{\dagger}` gate class"""
    gate_name = 'CT^\\dagger'
    gate_name_latex = r'\text{CT}^\dagger'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = TdgGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = TdgGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
