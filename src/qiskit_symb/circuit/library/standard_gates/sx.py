r"""Symbolic :math:`\sqrt{X}`, :math:`\sqrt{X}^{\dagger}`, controlled-:math:`\sqrt{X}`,
and controlled-:math:`\sqrt{X}^{\dagger}` gates module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class SXGate(Gate):
    r"""Symbolic :math:`\sqrt{X}` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='sx', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return 1/2 * Matrix([[1+i, 1-i],
                             [1-i, 1+i]])


class SXdgGate(Gate):
    r"""Symbolic :math:`\sqrt{X}^{\dagger}` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='sxdg', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return 1/2 * Matrix([[1-i, 1+i],
                             [1+i, 1-i]])


class CSXGate(ControlledGate):
    r"""Symbolic controlled-:math:`\sqrt{X}` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = SXGate()
        super().__init__(name='csx', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)


class CSXdgGate(ControlledGate):
    r"""Symbolic controlled-:math:`\sqrt{X}^{\dagger}` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = SXdgGate()
        super().__init__(name='csxdg', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
