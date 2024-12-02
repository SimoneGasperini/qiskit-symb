r"""Symbolic :math:`P(\lambda)` and controlled-:math:`P(\lambda)` gates module"""

from sympy import exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class PhaseGate(ParametricGate):
    r"""Symbolic :math:`P(\lambda)` gate class"""

    def __init__(self, lam, qubit):
        """todo"""
        params = (lam,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        lam, = self._get_params_expr()
        explam = exp(1j * lam)
        return Array([[1, 0],
                      [0, explam]])


class CPhaseGate(ParametricGate):
    r"""Symbolic controlled-:math:`P(\lambda)` gate class"""

    def __init__(self, lam, control, target):
        """todo"""
        params = (lam,)
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        lam, = self._get_params_expr()
        explam = exp(1j * lam)
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, explam]])
