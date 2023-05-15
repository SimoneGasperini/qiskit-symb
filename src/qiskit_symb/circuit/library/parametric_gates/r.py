r"""Symbolic :math:`R` and controlled-:math:`R` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class RGate(Gate):
    r"""Symbolic :math:`R(\theta, \phi)` gate class"""

    def __init__(self, theta, phi):
        """todo"""
        params = [theta, phi]
        super().__init__(name='r', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, phi = self._get_params_expr()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        return Matrix([[cos, -i * sympy.exp(-i * phi) * sin],
                       [-i * sympy.exp(i * phi) * sin, cos]])


class CRGate(ControlledGate):
    r"""Symbolic controlled-:math:`R` gate class"""

    def __init__(self, theta, phi, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        # pylint: disable=too-many-arguments
        params = [theta, phi]
        base_gate = RGate(theta, phi)
        super().__init__(name='cr', num_qubits=2, params=params,
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
