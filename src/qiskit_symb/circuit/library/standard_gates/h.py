r"""Symbolic Hadamard :math:`H` and controlled-:math:`H` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate
from ...controlledgate import ControlledGate


class HGate(StandardGate):
    r"""Symbolic math:`H` gate class"""
    gate_name = 'H'

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return 1/2**0.5 * Array([[1, 1],
                                 [1, -1]])


class CHGate(StandardGate, ControlledGate):
    r"""Symbolic controlled-:math:`H` gate class"""
    gate_name = 'CH'
    gate_name_latex = r'\text{CH}'

    def __new__(cls, control, target):
        """todo"""
        controls = (control,)
        target_gate = HGate(target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, control, target):
        """todo"""
        target_gate = HGate(target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
