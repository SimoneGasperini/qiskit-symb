r"""Symbolic two-qubits interaction :math:`XXPlusYYGate(\theta, \beta)` gate module"""

from sympy import Matrix, I, sin, cos, exp
from ...gate import ParametricGate


class XXPlusYYGate(ParametricGate):
    r"""Symbolic two-qubits interaction :math:`XXPlusYYGate(\theta, \beta)` gate class"""
    gate_name = 'XXpYY'
    gate_name_latex = 'XXpYY'

    def __new__(cls, theta, beta=0, *qubits):
        """todo"""
        params = (theta, beta)
        return super().__new__(cls, *qubits, params=params)

    @property
    def sympy_matrix(self):
        """todo"""
        theta, beta = self.get_params_expr()
        sympy_matrix = Matrix([[1, 0, 0, 0],
                               [0, cos(theta/2), -I*sin(theta/2)
                                * exp(-I*beta), 0],
                               [0, -I*sin(theta/2)*exp(I*beta),
                                cos(theta/2), 0],
                               [0, 0, 0, 1]])
        return sympy_matrix
