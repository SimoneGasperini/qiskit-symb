r"""Symbolic :math:`U(\theta, \phi, \lambda)` and
controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gates module"""

import sympy
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
        return sympy.exp(i * gamma) * Matrix([[cos, -sympy.exp(i*lam)*sin],
                                              [sympy.exp(i*phi)*sin, sympy.exp(i*(phi+lam))*cos]])


class CUGate(ControlledGate):
    r"""Symbolic controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gate class"""

    def __init__(self, theta, phi, lam, gamma=0, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        # pylint: disable=too-many-arguments
        base_gate = UGate(theta=theta, phi=phi, lam=lam, _gamma=gamma)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cu', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
