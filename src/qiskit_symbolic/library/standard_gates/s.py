r"""Symbolic :math:`S`, :math:`S^{\dagger}`, :math:`CS`, and :math:`CS^{\dagger}` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate
from qiskit_symbolic.controlledgate import ControlledGate


class SGate(Gate):
    r"""Symbolic :math:`S` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='s', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0],
                       [0, i]])


class SdgGate(Gate):
    r"""Symbolic :math:`S^{\dagger}` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='sdg', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0],
                       [0, -i]])


class CSGate(ControlledGate):
    r"""Symbolic :math:`CS` gate class"""

    def __init__(self, ctrl_qubit, tg_qubit):
        """todo"""
        super().__init__(name='cs', num_qubits=2, params=[],
                         ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, base_gate=SGate())


class CSdgGate(ControlledGate):
    r"""Symbolic :math:`CS^{\dagger}` gate class"""

    def __init__(self, ctrl_qubit, tg_qubit):
        """todo"""
        super().__init__(name='csdg', num_qubits=2, params=[],
                         ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, base_gate=SdgGate())
