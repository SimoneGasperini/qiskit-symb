r"""Symbolic two-qubits interaction :math:`XXPlusYYGate(\theta, \beta)` gate module"""

from sympy import sin, cos, exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class XXPlusYYGate(ParametricGate):
    r"""Symbolic two-qubits interaction :math:`XXPlusYYGate(\theta, \beta)` gate class"""

    def __init__(self, theta, beta, target1, target2):
        """todo"""
        params = (theta, beta)
        qubits = (target1, target2)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, beta = self._get_params_expr()
        costh2 = cos(theta / 2)
        isinth2 = 1j * sin(theta / 2)
        minusexp = exp(-1j * beta)
        plusexp = exp(1j * beta)
        return Array([[1, 0, 0, 0],
                      [0, costh2, -isinth2*minusexp, 0],
                      [0, -isinth2*plusexp, costh2, 0],
                      [0, 0, 0, 1]])
