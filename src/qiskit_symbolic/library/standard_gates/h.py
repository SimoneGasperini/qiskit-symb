r"""Symbolic Hadamard :math:`H` and :math:`CH` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate
from qiskit_symbolic.controlledgate import ControlledGate


class HGate(Gate):
    r"""Symbolic Hadamard :math:`H` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='h', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        return (1 / sympy.sqrt(2)) * Matrix([[1, 1],
                                             [1, -1]])


class CHGate(ControlledGate):
    r"""Symbolic :math:`CH` gate class"""

    def __init__(self, control_qubit=0, target_qubit=1):
        """todo"""
        base_gate = HGate()
        super().__init__(name='ch', num_qubits=2, params=[],
                         control_qubit=control_qubit, target_qubit=target_qubit,
                         base_gate=base_gate)
