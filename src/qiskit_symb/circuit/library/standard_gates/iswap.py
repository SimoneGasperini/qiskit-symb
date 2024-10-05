r"""Symbolic :math:`iSWAP` and controlled-:math:`iSWAP` gates module"""

from sympy import Matrix, I
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class iSwapGate(StandardGate):
    r"""Symbolic :math:`iSWAP` gate class"""
    gate_name = 'iSWAP'
    gate_name_latex = 'iSWAP'
    sympy_matrix = Matrix([[1, 0, 0, 0],
                           [0, 0, I, 0],
                           [0, I, 0, 0],
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
