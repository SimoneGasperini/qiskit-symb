r"""Symbolic :math:`RZ(\lambda)` and controlled-:math:`RZ(\lambda)` gates module"""

from sympy import exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class RZGate(ParametricGate):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""

    def __init__(self, lam, qubit):
        """todo"""
        params = (lam,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        lam, = self._get_params_expr()
        plusexp2 = exp(1j * lam/2)
        minusexp2 = exp(-1j * lam/2)
        return Array([[minusexp2, 0],
                      [0, plusexp2]])


class CRZGate(ParametricGate):
    r"""Symbolic controlled-:math:`RZ(\lambda)` gate class"""

    def __init__(self, lam, control, target):
        """todo"""
        params = (lam,)
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        lam, = self._get_params_expr()
        plusexp2 = exp(1j * lam/2)
        minusexp2 = exp(-1j * lam/2)
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, minusexp2, 0],
                      [0, 0, 0, plusexp2]])
