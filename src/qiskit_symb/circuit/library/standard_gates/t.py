r"""Symbolic :math:`T`, :math:`T^{\dagger}`, controlled-:math:`T`,
and controlled-:math:`T^{\dagger}` gates module"""

import sympy
from sympy.physics.quantum.gate import T
from ...gate import Gate
from ...controlledgate import ControlledGate


class TGate(Gate, T):
    r"""Symbolic :math:`T` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='t', sympy_name='T', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = self.get_target_matrix()
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix


class TdgGate(Gate):
    r"""Symbolic :math:`T^{\dagger}` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='tdg', sympy_name='T^\\dagger', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = TGate().__sympy__().H
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix


class CTGate(ControlledGate):
    r"""Symbolic controlled-:math:`T` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = TGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='ct', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)


class CTdgGate(ControlledGate):
    r"""Symbolic controlled-:math:`T^{\dagger}` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = TdgGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='ctdg', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
