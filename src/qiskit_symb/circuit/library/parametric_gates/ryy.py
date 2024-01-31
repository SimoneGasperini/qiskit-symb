r"""Symbolic :math:`RYY(\theta)` and controlled-:math:`RYY(\theta)` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class RYYGate(Gate):
    r"""Symbolic :math:`RYY(\theta)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='ryy', num_qubits=2, params=params)

    def __sympy__(self):
        """todo"""
        theta, = self._get_params_expr()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        return Matrix([[cos, 0, 0, i*sin],
                       [0, cos, -i*sin, 0],
                       [0, -i*sin, cos, 0],
                       [i*sin, 0, 0, cos]])


class CRYYGate(ControlledGate):
    r"""Symbolic controlled-:math:`RYY` gate class"""

    def __init__(self, theta, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = RYYGate(theta=theta)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cryy', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
