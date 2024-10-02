r"""Symbolic :math:`SWAP` and controlled-:math:`SWAP` gates module"""

import sympy
from sympy.physics.quantum.gate import SWAP
from ...gate import Gate
from ...controlledgate import ControlledGate


class SwapGate(Gate, SWAP):
    r"""Symbolic :math:`SWAP` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='swap', sympy_name='SWAP', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = self.get_target_matrix()
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix


class CSwapGate(ControlledGate):
    r"""Symbolic controlled-:math:`SWAP` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = SwapGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cswap', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
