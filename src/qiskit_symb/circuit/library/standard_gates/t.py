r"""Symbolic :math:`T`, :math:`T^{\dagger}`, controlled-:math:`T`,
and controlled-:math:`T^{\dagger}` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class TGate(Gate):
    r"""Symbolic :math:`T` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='t', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0],
                       [0, (1 + i) / sympy.sqrt(2)]])


class TdgGate(Gate):
    r"""Symbolic :math:`T^{\dagger}` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='tdg', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0],
                       [0, (1 - i) / sympy.sqrt(2)]])


class CTGate(ControlledGate):
    r"""Symbolic controlled-:math:`T` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = TGate()
        super().__init__(name='ct', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)


class CTdgGate(ControlledGate):
    r"""Symbolic controlled-:math:`T^{\dagger}` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = TdgGate()
        super().__init__(name='ctdg', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
