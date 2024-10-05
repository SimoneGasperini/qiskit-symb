r"""Symbolic Pauli :math:`Y` and controlled-:math:`Y` gates module"""

from sympy import Matrix, I
from sympy.physics.quantum.gate import Y
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class YGate(StandardGate, Y):
    r"""Symbolic Pauli math:`Y` gate class"""
    gate_name = 'Y'
    gate_name_latex = 'Y'
    sympy_matrix = Matrix([[0, -I],
                           [I, 0]])


class CYGate(ControlledGate):
    r"""Symbolic controlled-:math:`Y` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = YGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cy', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
