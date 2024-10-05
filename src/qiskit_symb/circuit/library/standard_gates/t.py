r"""Symbolic :math:`T`, :math:`T^{\dagger}`, controlled-:math:`T`,
and controlled-:math:`T^{\dagger}` gates module"""

from sympy import Matrix, I, pi, exp
from sympy.physics.quantum.gate import T
from ...gate import StandardGate
from ...controlledgate import ControlledGate


class TGate(StandardGate, T):
    r"""Symbolic :math:`T` gate class"""
    gate_name = 'T'
    gate_name_latex = 'T'
    sympy_matrix = Matrix([[1, 0],
                           [0, exp(I*pi/4)]])


class TdgGate(StandardGate):
    r"""Symbolic :math:`T^{\dagger}` gate class"""
    gate_name = 'T^\\dagger'
    gate_name_latex = 'T^\\dagger'
    sympy_matrix = TGate.sympy_matrix.H


class CTGate(ControlledGate):
    r"""Symbolic controlled-:math:`T` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = TGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='ct', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)


class CTdgGate(ControlledGate):
    r"""Symbolic controlled-:math:`T^{\dagger}` gate class"""

    def __init__(self, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = TdgGate()
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='ctdg', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
