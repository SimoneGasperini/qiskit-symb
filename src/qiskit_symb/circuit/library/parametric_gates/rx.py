r"""Symbolic :math:`RX(\theta)` and controlled-:math:`RX(\theta)` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class RXGate(Gate):
    r"""Symbolic :math:`RX(\theta)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='rx', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, = self._get_params_expr()
        i = sympy.I
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        return Matrix([[cos, -i * sin],
                       [-i * sin, cos]])


class CRXGate(ControlledGate):
    r"""Symbolic controlled-:math:`RX(\theta)` gate class"""

    def __init__(self, theta, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        params = [theta]
        base_gate = RXGate(theta)
        super().__init__(name='crx', num_qubits=2, params=params,
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
