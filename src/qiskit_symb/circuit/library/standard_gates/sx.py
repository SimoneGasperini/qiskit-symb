r"""Symbolic :math:`\sqrt{X}`, :math:`\sqrt{X}^{\dagger}`, controlled-:math:`\sqrt{X}`,
and controlled-:math:`\sqrt{X}^{\dagger}` gates module"""

from sympy import Matrix, I
from ...gate import StandardGate, ControlledGate


class SXGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}` gate class"""
    gate_name = '\sqrt X'
    gate_name_latex = r'\sqrt{\text{X}}'
    sympy_matrix = 1/2 * Matrix([[1+I, 1-I],
                                 [1-I, 1+I]])

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)


class SXdgGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}^{\dagger}` gate class"""
    gate_name = '\sqrt X^\dagger'
    gate_name_latex = r'\sqrt{\text{X}}^\dagger'
    sympy_matrix = SXGate.sympy_matrix.H

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)


class CSXGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`\sqrt{X}` gate class"""
    gate_name = 'C\sqrt X'
    gate_name_latex = r'\text{C}\sqrt{\text{X}}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = SXGate(target=target)
        return ControlledGate.__new__(cls, controls=controls, target_gate=target_gate)


class CSXdgGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`\sqrt{X}^{\dagger}` gate class"""
    gate_name = 'C\sqrt X^\dagger'
    gate_name_latex = r'\text{C}\sqrt{\text{X}}^\dagger'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = SXdgGate(target=target)
        return ControlledGate.__new__(cls, controls=controls, target_gate=target_gate)
