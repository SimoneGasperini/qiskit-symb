r"""Symbolic Pauli :math:`Z` and :math:`CZ` gates module"""

from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate
from qiskit_symbolic.controlledgate import ControlledGate


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
    r"""Symbolic :math:`CZ` gate class"""

    def __init__(self, control_qubit=0, target_qubit=1):
        """todo"""
        base_gate = ZGate()
        super().__init__(name='cz', num_qubits=2, params=[],
                         control_qubit=control_qubit, target_qubit=target_qubit,
                         base_gate=base_gate)
