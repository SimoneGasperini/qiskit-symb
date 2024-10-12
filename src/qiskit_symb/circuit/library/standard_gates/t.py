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
    sympy_matrix = Matrix([[1, 0],
                           [0, exp(I*pi/4)]])

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)


class TdgGate(StandardGate):
    r"""Symbolic :math:`T^{\dagger}` gate class"""
    gate_name = 'T^\dagger'
    gate_name_latex = r'\text{T}^\dagger'
    sympy_matrix = TGate.sympy_matrix.H

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)


class CTGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`T` gate class"""
    gate_name = 'CT'
    gate_name_latex = r'\text{CT}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = TGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)


class CTdgGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`T^{\dagger}` gate class"""
    gate_name = 'CT^\dagger'
    gate_name_latex = r'\text{CT}^\dagger'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = TdgGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)
