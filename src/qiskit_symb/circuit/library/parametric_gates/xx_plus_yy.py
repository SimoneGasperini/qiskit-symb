r"""Symbolic two-qubits interaction :math:`XXPlusYYGate(\theta, \beta)` gate module"""

from sympy import Matrix, I, sin, cos, exp
from ...gate import op00, op01, op10, op11
from ...parametricgate import ParametricGate


class XXPlusYYGate(ParametricGate):
    r"""Symbolic two-qubits interaction :math:`XXPlusYYGate(\theta, \beta)` gate class"""
    gate_name = 'XX+YY'
    gate_name_latex = r'\text{XX+YY}'

    def __new__(cls, theta, beta, target1, target2):
        """todo"""
        params = (theta, beta)
        qubits = (target1, target2)
        return super().__new__(cls, params=params, qubits=qubits)

    def __init__(self, theta, beta, target1, target2):
        """todo"""
        self.params = (theta, beta)
        self.qubits = (target1, target2)

    def _sympy_matrix(self):
        """todo"""
        theta, beta = self.get_params_expr()
        costh2 = cos(theta / 2)
        isinth2 = I * sin(theta / 2)
        minusexp = exp(-I * beta)
        plusexp = exp(I * beta)
        return Matrix([[1, 0, 0, 0],
                       [0, costh2, -isinth2*minusexp, 0],
                       [0, -isinth2*plusexp, costh2, 0],
                       [0, 0, 0, 1]])

    def _represent_ZGate(self, basis, **options):
        """todo"""
        theta, beta = self.get_params_expr()
        nqubits = options.get('nqubits', self.min_qubits)
        costh2 = cos(theta / 2)
        isinth2 = I * sin(theta / 2)
        minusexp = exp(-I * beta)
        plusexp = exp(I * beta)
        coeff_ops = [(1, (op00, op00)),
                     (costh2, (op11, op00)),
                     (costh2, (op00, op11)),
                     (1, (op11, op11)),
                     (-isinth2*minusexp, (op10, op01)),
                     (-isinth2*plusexp, (op01, op10))]
        matrix = self._define_matrix(coeff_ops=coeff_ops, nqubits=nqubits)
        return matrix
