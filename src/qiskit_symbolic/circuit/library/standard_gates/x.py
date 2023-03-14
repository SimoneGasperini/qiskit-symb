r"""Symbolic Pauli :math:`X` and :math:`CX` gates module"""

from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class XGate(Gate):
    r"""Symbolic Pauli :math:`X` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='x', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        return Matrix([[0, 1],
                       [1, 0]])


class CXGate(ControlledGate):
    r"""Symbolic :math:`CX` gate class"""

    def __init__(self, control_qubit=0, target_qubit=1):
        """todo"""
        base_gate = XGate()
        super().__init__(name='cx', num_qubits=2, params=[],
                         control_qubit=control_qubit, target_qubit=target_qubit,
                         base_gate=base_gate)
