r"""Symbolic :math:`RZ(\phi)` and controlled-:math:`RZ(\phi)` gates module"""

from sympy import Matrix, I, exp
from ...gate import ParametricGate
from ...controlledgate import ControlledGate


class RZGate(ParametricGate):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""
    gate_name = 'RZ'
    gate_name_latex = 'RZ'

    def __new__(cls, phi, *qubits):
        """todo"""
        params = (phi,)
        return super().__new__(cls, *qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        lam, = self.get_params_expr()
        sympy_matrix = Matrix([[exp(-I*lam/2), 0],
                               [0, exp(I*lam/2)]])
        return sympy_matrix


class CRZGate(ControlledGate):
    r"""Symbolic controlled-:math:`RZ(\phi)` gate class"""

    def __init__(self, phi, num_ctrl_qubits=1, ctrl_state=None):
        """todo"""
        base_gate = RZGate(phi=phi)
        num_qubits = num_ctrl_qubits + base_gate.num_qubits
        params = base_gate.params
        super().__init__(name='crz', num_qubits=num_qubits, params=params, base_gate=base_gate,
                         num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
