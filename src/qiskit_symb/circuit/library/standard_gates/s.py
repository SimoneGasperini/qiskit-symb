r"""Symbolic :math:`S`, :math:`S^{\dagger}`, controlled-:math:`S`,
and controlled-:math:`S^{\dagger}` gates module"""

from sympy import Matrix, I
from sympy.physics.quantum.gate import S
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class SGate(StandardGate, S):
    r"""Symbolic :math:`S` gate class"""
    gate_name = 'S'
    gate_name_latex = r'\text{S}'

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
                       [0, I]])


class SdgGate(StandardGate):
    r"""Symbolic :math:`S^{\dagger}` gate class"""
    gate_name = 'S^\\dagger'
    gate_name_latex = r'\text{S}^\dagger'

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
        return SGate._sympy_matrix().H


class CSGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`S` gate class"""
    gate_name = 'CS'
    gate_name_latex = r'\text{CS}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = SGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = SGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)


class CSdgGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`S^{\dagger}` gate class"""
    gate_name = 'CS^\\dagger'
    gate_name_latex = r'\text{CS}^\dagger'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = SdgGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = SdgGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
