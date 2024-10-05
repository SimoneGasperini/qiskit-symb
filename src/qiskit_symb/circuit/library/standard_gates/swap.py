r"""Symbolic :math:`SWAP` and controlled-:math:`SWAP` gates module"""

from sympy import Matrix
from sympy.physics.quantum.gate import SWAP
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class SwapGate(StandardGate, SWAP):
    r"""Symbolic :math:`SWAP` gate class"""
    gate_name = 'SWAP'
    gate_name_latex = 'SWAP'
    sympy_matrix = Matrix([[1, 0, 0, 0],
                           [0, 0, 1, 0],
                           [0, 1, 0, 0],
                           [0, 0, 0, 1]])


class CSwapGate(ControlledGate):
    r"""Symbolic controlled-:math:`SWAP` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = SwapGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cswap', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
