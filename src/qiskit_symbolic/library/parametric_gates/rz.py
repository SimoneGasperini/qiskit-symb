r"""Symbolic :math:`RZ(\phi)` and :math:`CRZ(\phi)` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate
from qiskit_symbolic.controlledgate import ControlledGate


class RZGate(Gate):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""

    def __init__(self, phi):
        """todo"""
        params = [phi]
        super().__init__(name='rz', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        lam, = self.get_sympy_params()
        i = sympy.I
        return Matrix([[sympy.exp(-i * lam/2), 0],
                       [0, sympy.exp(i * lam/2)]])


class CRZGate(ControlledGate):
    r"""Symbolic :math:`CRZ(\phi)` gate class"""

    def __init__(self, phi, ctrl_qubit, tg_qubit):
        """todo"""
        params = [phi]
        base_gate = RZGate(phi)
        super().__init__(name='crz', num_qubits=2, params=params,
                         ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, base_gate=base_gate)
