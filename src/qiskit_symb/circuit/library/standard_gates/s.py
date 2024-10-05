r"""Symbolic :math:`S`, :math:`S^{\dagger}`, controlled-:math:`S`,
and controlled-:math:`S^{\dagger}` gates module"""

from sympy import Matrix, I
from sympy.physics.quantum.gate import S
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class SGate(StandardGate, S):
    r"""Symbolic :math:`S` gate class"""
    gate_name = 'S'
    gate_name_latex = 'S'
    sympy_matrix = Matrix([[1, 0],
                           [0, I]])


class SdgGate(StandardGate):
    r"""Symbolic :math:`S^{\dagger}` gate class"""
    gate_name = 'S^\\dagger'
    gate_name_latex = 'S^\\dagger'
    sympy_matrix = SGate.sympy_matrix.H


class CSGate(ControlledGate):
    r"""Symbolic controlled-:math:`S` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = SGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='cs', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)


class CSdgGate(ControlledGate):
    r"""Symbolic controlled-:math:`S^{\dagger}` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        base_gate = SdgGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='csdg', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
