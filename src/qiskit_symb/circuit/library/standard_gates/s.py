r"""Symbolic :math:`S`, :math:`S^{\dagger}`, controlled-:math:`S`,
and controlled-:math:`S^{\dagger}` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


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
    r"""Symbolic controlled-:math:`S` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = SGate()
        super().__init__(name='cs', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)


class CSdgGate(ControlledGate):
    r"""Symbolic controlled-:math:`S^{\dagger}` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = SdgGate()
        super().__init__(name='csdg', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
