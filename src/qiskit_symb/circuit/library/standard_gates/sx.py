r"""Symbolic :math:`\sqrt{X}`, :math:`\sqrt{X}^{\dagger}`, controlled-:math:`\sqrt{X}`,
and controlled-:math:`\sqrt{X}^{\dagger}` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class SXGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}` gate class"""
    gate_name = '\\sqrt X'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return 0.5 * Array([[1+1j, 1-1j],
                            [1-1j, 1+1j]])


class SXdgGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}^{\dagger}` gate class"""
    gate_name = '\\sqrt X^\\dagger'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return 0.5 * Array([[1-1j, 1+1j],
                            [1+1j, 1-1j]])


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
