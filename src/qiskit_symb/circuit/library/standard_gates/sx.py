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

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = SXGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='csx', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)


class CSXdgGate(ControlledGate):
    r"""Symbolic controlled-:math:`\sqrt{X}^{\dagger}` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = SXdgGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='csxdg', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
