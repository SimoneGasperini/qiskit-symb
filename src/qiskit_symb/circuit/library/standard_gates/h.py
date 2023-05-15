r"""Symbolic Hadamard :math:`H` and controlled-:math:`H` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class HGate(Gate):
    r"""Symbolic Hadamard :math:`H` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='h', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        return (1 / sympy.sqrt(2)) * Matrix([[1, 1],
                                             [1, -1]])


class CHGate(ControlledGate):
    r"""Symbolic controlled:math:`H` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = HGate()
        super().__init__(name='ch', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
