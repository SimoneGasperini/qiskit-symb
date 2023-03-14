r"""Symbolic Pauli :math:`Y` and :math:`CY` gates module"""

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
    r"""Symbolic :math:`CY` gate class"""

    def __init__(self, control_qubit=0, target_qubit=1):
        """todo"""
        base_gate = YGate()
        super().__init__(name='cy', num_qubits=2, params=[],
                         control_qubit=control_qubit, target_qubit=target_qubit,
                         base_gate=base_gate)
