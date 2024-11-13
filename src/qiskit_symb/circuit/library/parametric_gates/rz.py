r"""Symbolic :math:`RZ(\phi)` and controlled-:math:`RZ(\phi)` gates module"""

from sympy import Matrix, I, exp
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class RZGate(ParametricGate):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""
    gate_name = 'RZ'
    gate_name_latex = r'\text{RZ}'

    def __new__(cls, phi, target):
        """todo"""
        params = (phi,)
        qubits = (target,)
        return super().__new__(cls, params=params, qubits=qubits)

    def __init__(self, phi, target):
        """todo"""
        self.params = (phi,)
        self.qubits = (target,)

    def _sympy_matrix(self):
        """todo"""
        lam, = self.get_params_expr()
        plusexp2 = exp(I * lam/2)
        minusexp2 = exp(-I * lam/2)
        return Matrix([[minusexp2, 0],
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
