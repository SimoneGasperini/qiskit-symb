r"""Symbolic :math:`\sqrt{X}`, :math:`\sqrt{X}^{\dagger}`, controlled-:math:`\sqrt{X}`,
and controlled-:math:`\sqrt{X}^{\dagger}` gates module"""

from sympy import Matrix, I
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class SXGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}` gate class"""
    gate_name = '\\sqrt X'
    gate_name_latex = '\\sqrt X'
    sympy_matrix = 1/2 * Matrix([[1+I, 1-I],
                                 [1-I, 1+I]])


class SXdgGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}^{\dagger}` gate class"""
    gate_name = '\\sqrt X^\\dagger'
    gate_name_latex = '\\sqrt X^\\dagger'
    sympy_matrix = SXGate.sympy_matrix.H


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
