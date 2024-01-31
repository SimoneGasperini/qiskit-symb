r"""Symbolic :math:`RZZ(\theta)` and controlled-:math:`RZZ(\theta)` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class RZZGate(Gate):
    r"""Symbolic :math:`RZZ(\theta)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='rzz', num_qubits=2, params=params)

    def __sympy__(self):
        """todo"""
        theta, = self._get_params_expr()
        i = sympy.I
        return Matrix([[sympy.exp(-i*theta/2), 0, 0, 0],
                       [0, sympy.exp(i*theta/2), 0, 0],
                       [0, 0, sympy.exp(i*theta/2), 0],
                       [0, 0, 0, sympy.exp(-i*theta/2)]])


class CRZZGate(ControlledGate):
    r"""Symbolic controlled-:math:`RZZ` gate class"""

    def __init__(self, theta, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = RZZGate(theta=theta)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='crzz', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
