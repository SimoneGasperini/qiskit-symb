r"""Symbolic :math:`S`, :math:`S^{\dagger}`, controlled-:math:`S`,
and controlled-:math:`S^{\dagger}` gates module"""

import sympy
from sympy.physics.quantum.gate import S
from ...gate import Gate
from ...controlledgate import ControlledGate


class SGate(Gate, S):
    r"""Symbolic :math:`S` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='s', sympy_name='S', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = self.get_target_matrix()
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix


class SdgGate(Gate):
    r"""Symbolic :math:`S^{\dagger}` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(qiskit_name='sdg', sympy_name='S^\\dagger', params=())

    def __sympy__(self):
        """todo"""
        sympy_matrix = SGate().__sympy__().H
        return sympy_matrix

    def __numpy__(self):
        """todo"""
        sympy_matrix = self.__sympy__()
        numpy_matrix = sympy.matrix2numpy(sympy_matrix, dtype=complex)
        return numpy_matrix


class CSGate(ControlledGate):
    r"""Symbolic controlled-:math:`S` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = SGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cs', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)


class CSdgGate(ControlledGate):
    r"""Symbolic controlled-:math:`S^{\dagger}` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        base_gate = SdgGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='csdg', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
