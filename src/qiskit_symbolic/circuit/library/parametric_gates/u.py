r"""Symbolic :math:`U(\theta, \phi, \lambda)` and
controlled-:math:`U(\theta, \phi, \lambda)` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class UGate(Gate):
    r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate class"""

    def __init__(self, theta, phi, lam):
        """todo"""
        params = [theta, phi, lam]
        super().__init__(name='u', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, phi, lam = self._get_params_expr()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        exp = sympy.exp
        return Matrix([[cos, -exp(i * lam) * sin],
                       [exp(i * phi) * sin, exp(i * (phi + lam)) * cos]])


class CUGate(ControlledGate):
    r"""Symbolic controlled-:math:`U(\theta, \phi, \lambda)` gate class"""

    def __init__(self, theta, phi, lam, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        # pylint: disable=too-many-arguments
        params = [theta, phi, lam]
        base_gate = UGate(theta, phi, lam)
        super().__init__(name='cu', num_qubits=2, params=params,
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
