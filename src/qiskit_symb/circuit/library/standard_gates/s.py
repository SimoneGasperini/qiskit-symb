r"""Symbolic :math:`S`, :math:`S^{\dagger}`, controlled-:math:`S`,
and controlled-:math:`S^{\dagger}` gates module"""

from sympy.tensor.array import Array
from sympy.physics.quantum.gate import S
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class SGate(StandardGate, S):
    r"""Symbolic :math:`S` gate class"""
    gate_name = 'S'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, 1j]])


class SdgGate(StandardGate):
    r"""Symbolic :math:`S^{\dagger}` gate class"""
    gate_name = 'S^\\dagger'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, -1j]])


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
