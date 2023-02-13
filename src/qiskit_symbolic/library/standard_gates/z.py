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

    def __init__(self, ctrl_qubit=0, tg_qubit=1):
        """todo"""
        super().__init__(name='cz', num_qubits=2, params=[],
                         ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, base_gate=ZGate())
