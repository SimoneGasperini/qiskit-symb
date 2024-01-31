r"""Symbolic Pauli :math:`Z` and controlled-:math:`Z` gates module"""

from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class ZGate(Gate):
    r"""Symbolic Pauli :math:`Z` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='z', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        return Matrix([[1, 0],
                       [0, -1]])


class CZGate(ControlledGate):
    r"""Symbolic controlled-:math:`Z` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = ZGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cz', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
