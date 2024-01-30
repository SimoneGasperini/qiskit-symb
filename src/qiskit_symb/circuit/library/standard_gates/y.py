r"""Symbolic Pauli :math:`Y` and controlled-:math:`Y` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class YGate(Gate):
    r"""Symbolic Pauli :math:`Y` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='y', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[0, -i],
                       [i, 0]])


class CYGate(ControlledGate):
    r"""Symbolic controlled-:math:`Y` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = YGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cy', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
