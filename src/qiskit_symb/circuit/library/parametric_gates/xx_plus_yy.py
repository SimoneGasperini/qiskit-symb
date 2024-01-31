r"""Symbolic two-qubits interaction :math:`XXPlusYYGate(\theta, \beta)` gate module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate


class XXPlusYYGate(Gate):
    r"""Symbolic two-qubits interaction :math:`XXPlusYYGate(\theta, \beta)` gate class"""

    def __init__(self, theta, beta=0):
        """todo"""
        params = [theta, beta]
        super().__init__(name='xx_plus_yy', num_qubits=2, params=params)

    def __sympy__(self):
        """todo"""
        theta, beta = self._get_params_expr()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        return Matrix([[1, 0, 0, 0],
                       [0, cos, -i * sin * sympy.exp(-i * beta), 0],
                       [0, -i * sin * sympy.exp(i * beta), cos, 0],
                       [0, 0, 0, 1]])
