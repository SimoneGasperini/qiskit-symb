r"""Symbolic :math:`U(\theta, \phi, \lambda)` and
controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gates module"""

import sympy
from sympy import sqrt
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class UGate(Gate):
    r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate class"""

    def __init__(self, theta, phi, lam, _gamma=0):
        """todo"""
        params = [theta, phi, lam, _gamma]
        super().__init__(name='u', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, phi, lam, gamma = self._get_params_expr()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        exp = sympy.exp
        return exp(i * gamma) * Matrix([[cos, -exp(i * lam) * sin],
                                        [exp(i * phi) * sin, exp(i * (phi + lam)) * cos]])


class U1Gate(Gate):
    r"""Symbolic :math:`U1(\lambda)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='u1', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        lam = self._get_params_expr()[0]
        i = sympy.I
        exp = sympy.exp
        return Matrix([[1, 0],[0, exp(i*lam)]])


class CU1Gate(ControlledGate):
    r"""Symbolic controlled-:math:`U(\lambda)` gate class"""

    def __init__(self, theta,
                 ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        # pylint: disable=too-many-arguments
        params = [theta]
        base_gate = U1Gate(theta)
        super().__init__(name='cu1', num_qubits=2, params=params,
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)


class U2Gate(Gate):
    r"""Symbolic :math:`U2(\theta, \phi)` gate class"""

    def __init__(self, theta, phi):
        """todo"""
        params = [theta, phi]
        super().__init__(name='u2', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        isqrt2 = 1 / sqrt(2)
        phi, lam = self._get_params_expr()

        i = sympy.I
        exp = sympy.exp
        return Matrix(
            [
                [isqrt2, -exp(i * lam) * isqrt2],
                [exp(i * phi) * isqrt2, exp(i * (phi + lam)) * isqrt2],
            ])


class CUGate(ControlledGate):
    r"""Symbolic controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gate class"""

    def __init__(self, theta, phi, lam, gamma=0,
                 ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        # pylint: disable=too-many-arguments
        params = [theta, phi, lam, gamma]
        base_gate = UGate(theta, phi, lam, gamma)
        super().__init__(name='cu', num_qubits=2, params=params,
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
