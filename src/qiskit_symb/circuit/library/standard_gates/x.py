r"""Symbolic Pauli :math:`X` and controlled-:math:`X` gates module"""

import sympy
from sympy.physics.quantum.gate import X
from ...gate import Gate
from ...controlledgate import ControlledGate


class XGate(Gate, X):
    r"""Symbolic Pauli :math:`X` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='x', sympy_name='X', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = self.get_target_matrix()
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix


class CXGate(ControlledGate):
    r"""Symbolic controlled-:math:`X` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = XGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cx', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
