r"""Symbolic :math:`P(\lambda)` and controlled-:math:`P(\lambda)` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class PhaseGate(Gate):
    r"""Symbolic :math:`P(\lambda)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='p', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        lam, = self._get_params_expr()
        i = sympy.I
        return Matrix([[1, 0],
                       [0, sympy.exp(i*lam)]])


class CPhaseGate(ControlledGate):
    r"""Symbolic controlled-:math:`P(\lambda)` gate class"""

    def __init__(self, theta, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = PhaseGate(theta=theta)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cp', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
