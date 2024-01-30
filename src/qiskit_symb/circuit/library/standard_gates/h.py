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
        return 1/sympy.sqrt(2) * Matrix([[1, 1],
                                         [1, -1]])


class CHGate(ControlledGate):
    r"""Symbolic controlled:math:`H` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = HGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='ch', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state,)
