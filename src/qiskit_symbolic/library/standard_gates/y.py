r"""Symbolic Pauli :math:`Y` and :math:`CY` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate
from qiskit_symbolic.controlledgate import ControlledGate


class YGate(Gate):
    r"""Symbolic Pauli :math:`Y` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='y', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[0, -i],
                       [i, 0]])


class CYGate(ControlledGate):
    r"""Symbolic :math:`CY` gate class"""

    def __init__(self, ctrl_qubit=0, tg_qubit=1):
        """todo"""
        super().__init__(name='cy', num_qubits=2, params=[],
                         ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, base_gate=YGate())
