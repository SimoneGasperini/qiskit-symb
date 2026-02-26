r"""Symbolic :math:`(XX+YY)(\theta,\beta)` gate module."""

from sympy import cos, exp, sin
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class XXPlusYYGate(ParametricGate):
    r"""Symbolic :math:`(XX+YY)(\theta,\beta)` gate class."""

    def __init__(self, theta, beta, qubit1, qubit2):
        """todo"""
        params = (theta, beta)
        qubits = (qubit1, qubit2)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, beta = self._get_params_expr()
        costh2 = cos(theta / 2)
        isinth2 = 1j * sin(theta / 2)
        return Array(
            [
                [1, 0, 0, 0],
                [0, costh2, -isinth2 * exp(-1j * beta), 0],
                [0, -isinth2 * exp(1j * beta), costh2, 0],
                [0, 0, 0, 1],
            ]
        )
