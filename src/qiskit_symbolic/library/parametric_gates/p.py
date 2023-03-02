r"""Symbolic :math:`P(\lambda)` and :math:`CP(\lambda)` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate
from qiskit_symbolic.controlledgate import ControlledGate


class PhaseGate(Gate):
    r"""Symbolic :math:`P(\lambda)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='p', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        lam, = self._get_params_expr()
        i = sympy.I
        return Matrix([[1, 0],
                       [0, sympy.exp(i * lam)]])


class CPhaseGate(ControlledGate):
    r"""Symbolic :math:`CP(\lambda)` gate class"""

    def __init__(self, theta, ctrl_qubit=0, tg_qubit=1):
        """todo"""
        params = [theta]
        base_gate = PhaseGate(theta)
        super().__init__(name='cp', num_qubits=2, params=params,
                         ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, base_gate=base_gate)
