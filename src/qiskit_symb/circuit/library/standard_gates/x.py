r"""Symbolic Pauli :math:`X` and controlled-:math:`X` gates module"""

from sympy import Matrix
from sympy.physics.quantum.gate import X
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class XGate(StandardGate, X):
    r"""Symbolic Pauli math:`X` gate class"""
    gate_name = 'X'
    gate_name_latex = 'X'
    sympy_matrix = Matrix([[0, 1],
                           [1, 0]])


class CXGate(ControlledGate):
    r"""Symbolic controlled-:math:`X` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = XGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cx', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
