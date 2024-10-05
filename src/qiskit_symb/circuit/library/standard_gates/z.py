r"""Symbolic Pauli :math:`Z` and controlled-:math:`Z` gates module"""

from sympy import Matrix
from sympy.physics.quantum.gate import Z
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class ZGate(StandardGate, Z):
    r"""Symbolic Pauli math:`Z` gate class"""
    gate_name = 'Z'
    gate_name_latex = 'Z'
    sympy_matrix = Matrix([[1, 0],
                           [0, -1]])


class CZGate(ControlledGate):
    r"""Symbolic controlled-:math:`Z` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = ZGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cz', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
