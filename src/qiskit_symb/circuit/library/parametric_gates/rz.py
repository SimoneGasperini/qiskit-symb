r"""Symbolic :math:`RZ(\phi)` and controlled-:math:`RZ(\phi)` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class RZGate(Gate):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""

    def __init__(self, phi):
        """todo"""
        params = [phi]
        super().__init__(name='rz', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        lam, = self._get_params_expr()
        i = sympy.I
        return Matrix([[sympy.exp(-i*lam/2), 0],
                       [0, sympy.exp(i*lam/2)]])


class CRZGate(ControlledGate):
    r"""Symbolic controlled-:math:`RZ(\phi)` gate class"""

    def __init__(self, phi, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = RZGate(phi=phi)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='crz', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
