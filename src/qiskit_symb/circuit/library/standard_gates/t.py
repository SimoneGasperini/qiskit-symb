r"""Symbolic :math:`T`, :math:`T^{\dagger}`, controlled-:math:`T`,
and controlled-:math:`T^{\dagger}` gates module"""

from numpy import pi
from sympy import exp
from sympy.tensor.array import Array
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class TGate(StandardGate):
    r"""Symbolic :math:`T` gate class"""
    gate_name = 'T'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, exp(1j*pi/4)]])


class TdgGate(StandardGate):
    r"""Symbolic :math:`T^{\dagger}` gate class"""
    gate_name = 'T^\\dagger'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, exp(-1j*pi/4)]])


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
