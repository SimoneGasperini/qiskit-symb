r"""Symbolic Hadamard :math:`H` and controlled-:math:`H` gates module"""

from sympy import Matrix, sqrt
from sympy.physics.quantum.gate import H
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class HGate(StandardGate, H):
    r"""Symbolic math:`H` gate class"""
    gate_name = 'H'
    gate_name_latex = 'H'
    sympy_matrix = 1/sqrt(2) * Matrix([[1, 1],
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
