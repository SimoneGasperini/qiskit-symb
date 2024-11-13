r"""Symbolic :math:`\sqrt{X}`, :math:`\sqrt{X}^{\dagger}`, controlled-:math:`\sqrt{X}`,
and controlled-:math:`\sqrt{X}^{\dagger}` gates module"""

from sympy import Matrix, I, Rational
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class SXGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}` gate class"""
    gate_name = '\\sqrt X'
    gate_name_latex = r'\sqrt{\text{X}}'

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
        return Rational(1, 2) * Matrix([[1+I, 1-I],
                                        [1-I, 1+I]])


class SXdgGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}^{\dagger}` gate class"""
    gate_name = '\\sqrt X^\\dagger'
    gate_name_latex = r'\sqrt{\text{X}}^\dagger'

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
        return SXGate._sympy_matrix().H


class CSXGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`\sqrt{X}` gate class"""
    gate_name = 'C\\sqrt X'
    gate_name_latex = r'\text{C}\sqrt{\text{X}}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = SXGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = SXGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)


class CSXdgGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`\sqrt{X}^{\dagger}` gate class"""
    gate_name = 'C\\sqrt X^\\dagger'
    gate_name_latex = r'\text{C}\sqrt{\text{X}}^\dagger'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = SXdgGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = SXdgGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
