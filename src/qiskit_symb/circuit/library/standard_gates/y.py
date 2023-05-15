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

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = YGate()
        super().__init__(name='cy', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
