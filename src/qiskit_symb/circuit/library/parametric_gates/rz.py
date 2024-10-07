r"""Symbolic :math:`RZ(\phi)` and controlled-:math:`RZ(\phi)` gates module"""

from sympy import Matrix, I, exp
from ...gate import ParametricGate, ControlledGate


class RZGate(ParametricGate):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""
    gate_name = 'RZ'
    gate_name_latex = r'\text{RZ}'

    def __new__(cls, phi, target):
        """todo"""
        qubits = (target,)
        params = (phi,)
        return super().__new__(cls, qubits=qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        lam, = self.get_params_expr()
        return Matrix([[exp(-I*lam/2), 0],
                       [0, exp(I*lam/2)]])


class CRZGate(ParametricGate, ControlledGate):
    r"""Symbolic controlled-:math:`RZ(\phi)` gate class"""
    gate_name = 'CRZ'
    gate_name_latex = r'\text{CRZ}'

    def __new__(cls, phi, control, target):
        """todo"""
        controls = (control,)
        target_gate = RZGate(phi=phi, target=target)
        return ControlledGate.__new__(cls, controls=controls, target_gate=target_gate)
