r"""Symbolic two-qubits interaction :math:`XXMinusYYGate(\theta, \beta)` gate module"""

import sympy
from sympy.matrices import Matrix
from ...gate import Gate


class XXMinusYYGate(Gate):
    r"""Symbolic two-qubits interaction :math:`XXMinusYYGate(\theta, \beta)` gate class"""

    def __init__(self, theta, beta=0, qubits=None):
        """todo"""
        params = [theta, beta]
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='xx_minus_yy', num_qubits=2, params=params, qubits=qubits)

    def __sympy__(self):
        """todo"""
        theta, beta = self._get_params_expr()
        cos = sympy.cos(theta/2)
        sin = sympy.sin(theta/2)
        return Matrix([
            [cos, 0, 0, -sympy.I * sin * sympy.exp(-sympy.I * beta)],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-sympy.I * sin * sympy.exp(sympy.I * beta), 0, 0, cos],
        ])
