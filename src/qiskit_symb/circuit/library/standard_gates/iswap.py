r"""Symbolic :math:`iSWAP` and controlled-:math:`iSWAP` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


# pylint: disable=invalid-name
class iSwapGate(Gate):
    r"""Symbolic :math:`iSWAP` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='iswap', num_qubits=2, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0, 0, 0],
                       [0, 0, i, 0],
                       [0, i, 0, 0],
                       [0, 0, 0, 1]])


class CiSwapGate(ControlledGate):
    r"""Symbolic controlled-:math:`iSWAP` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = iSwapGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='ciswap', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
