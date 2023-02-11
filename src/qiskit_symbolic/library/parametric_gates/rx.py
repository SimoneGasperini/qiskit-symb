r"""Symbolic :math:`RX(\theta)` and :math:`CRX(\theta)` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate
from qiskit_symbolic.controlledgate import ControlledGate


class RXGate(Gate):
    r"""Symbolic :math:`RX(\theta)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='rx', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, = self.get_sympy_params()
        i = sympy.I
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        return Matrix([[cos, -i * sin],
                       [-i * sin, cos]])


class CRXGate(ControlledGate):
    r"""Symbolic :math:`CRX(\theta)` gate class"""

    def __init__(self, theta, ctrl_qubit, tg_qubit):
        """todo"""
        params = [theta]
        base_gate = RXGate(theta)
        super().__init__(name='crx', num_qubits=2, params=params,
                         ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, base_gate=base_gate)
