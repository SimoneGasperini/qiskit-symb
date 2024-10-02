r"""Symbolic Pauli :math:`Y` and controlled-:math:`Y` gates module"""

import sympy
from sympy.physics.quantum.gate import Y
from ...gate import Gate
from ...controlledgate import ControlledGate


class YGate(Gate, Y):
    r"""Symbolic Pauli :math:`Y` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='y', sympy_name='Y', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = self.get_target_matrix()
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix


class CYGate(ControlledGate):
    r"""Symbolic controlled-:math:`Y` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = YGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cy', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
