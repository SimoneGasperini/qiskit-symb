r"""Symbolic :math:`U(\theta, \phi, \lambda)` and
controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gates module"""

from sympy import Matrix, I, sin, cos, exp
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class UGate(ParametricGate):
    r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate class"""
    gate_name = 'U'
    gate_name_latex = r'\text{U}'

    def __new__(cls, theta, phi, lam, target, _gamma=0):
        """todo"""
        qubits = (target,)
        params = (theta, phi, lam, _gamma)
        return super().__new__(cls, qubits=qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, phi, lam, gamma = self.get_params_expr()
        return exp(I * gamma) * Matrix([[cos(theta/2), -exp(I*lam)*sin(theta/2)],
                                        [exp(I*phi)*sin(theta/2), exp(I*(phi+lam))*cos(theta/2)]])


class CUGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gate class"""
    gate_name = 'CU'
    gate_name_latex = r'\text{CU}'

    def __new__(cls, theta, phi, lam, gamma, control, target):
        """todo"""
        controls = (control,)
        target_gate = UGate(theta=theta, phi=phi, lam=lam,
                            _gamma=gamma, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)
