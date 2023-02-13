r"""Symbolic Pauli :math:`X` and :math:`CX` gates module"""

from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate
from qiskit_symbolic.controlledgate import ControlledGate


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

    def __init__(self, ctrl_qubit=0, tg_qubit=1):
        """todo"""
        super().__init__(name='cx', num_qubits=2, params=[],
                         ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, base_gate=XGate())
