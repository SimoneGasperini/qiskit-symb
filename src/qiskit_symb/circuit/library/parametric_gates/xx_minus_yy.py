r"""Symbolic two-qubits interaction :math:`XXMinusYYGate(\theta, \beta)` gate module"""

from sympy import Matrix, I, sin, cos, exp
from ...gate import ParametricGate


class XXMinusYYGate(ParametricGate):
    r"""Symbolic two-qubits interaction :math:`XXMinusYYGate(\theta, \beta)` gate class"""
    gate_name = 'XXmYY'
    gate_name_latex = 'XXmYY'

    def __new__(cls, theta, beta=0, *qubits):
        """todo"""
        params = (theta, beta)
        return super().__new__(cls, *qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, beta = self.get_params_expr()
        sympy_matrix = Matrix([[cos(theta/2), 0, 0, -I*sin(theta/2)*exp(-I*beta)],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [-I*sin(theta/2)*exp(I*beta), 0, 0, cos(theta/2)]])
        return sympy_matrix
