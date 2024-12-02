r"""Symbolic :math:`RZ(\lambda)` and controlled-:math:`RZ(\lambda)` gates module"""

from sympy import exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class RZGate(ParametricGate):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""
    gate_name = 'RZ'

    def __init__(self, lam, qubit):
        """todo"""
        params = (lam,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        lam, = self.params
        plusexp2 = exp(1j * lam/2)
        minusexp2 = exp(-1j * lam/2)
        return Array([[minusexp2, 0],
                      [0, plusexp2]])


class CRZGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`RZ(\phi)` gate class"""
    gate_name = 'CRZ'
    gate_name_latex = r'\text{CRZ}'

    def __new__(cls, phi, control, target):
        """todo"""
        controls = (control,)
        target_gate = RZGate(phi=phi, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, phi, control, target):
        """todo"""
        target_gate = RZGate(phi=phi, target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
