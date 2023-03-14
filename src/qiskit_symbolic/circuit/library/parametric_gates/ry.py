r"""Symbolic :math:`RY(\theta)` and :math:`CRY(\theta)` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class RYGate(Gate):
    r"""Symbolic :math:`RY(\theta)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='ry', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, = self._get_params_expr()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        return Matrix([[cos, -sin],
                       [sin, cos]])


class CRYGate(ControlledGate):
    r"""Symbolic :math:`CRY(\theta)` gate class"""

    def __init__(self, theta, control_qubit=0, target_qubit=1):
        """todo"""
        params = [theta]
        base_gate = RYGate(theta)
        super().__init__(name='cry', num_qubits=2, params=params,
                         control_qubit=control_qubit, target_qubit=target_qubit,
                         base_gate=base_gate)
