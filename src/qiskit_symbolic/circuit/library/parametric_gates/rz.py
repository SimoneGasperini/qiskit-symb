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
        return Matrix([[sympy.exp(-i * lam/2), 0],
                       [0, sympy.exp(i * lam/2)]])


class CRZGate(ControlledGate):
    r"""Symbolic controlled-:math:`RZ(\phi)` gate class"""

    def __init__(self, phi, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        params = [phi]
        base_gate = RZGate(phi)
        super().__init__(name='crz', num_qubits=2, params=params,
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
