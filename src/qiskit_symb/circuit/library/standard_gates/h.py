r"""Symbolic Hadamard :math:`H` and controlled-:math:`H` gates module"""

import sympy
from sympy.physics.quantum.gate import H
from ...gate import Gate
from ...controlledgate import ControlledGate


class HGate(Gate, H):
    def __init__(self):
        super().__init__(qiskit_name='h', sympy_name='H', params=())

    def __sympy__(self):
        sympy_matrix = self.get_target_matrix()
        return sympy_matrix

    def __numpy__(self):
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix


class CHGate(ControlledGate):
    r"""Symbolic controlled:math:`H` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = HGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='ch', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state,)
