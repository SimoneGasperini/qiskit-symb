r"""Symbolic :math:`RZZ(\theta)` and controlled-:math:`RZZ(\theta)` gates module"""

from sympy import Matrix, I, exp
from ...gate import op00, op11
from ...parametricgate import ParametricGate


class RZZGate(ParametricGate):
    r"""Symbolic :math:`RZZ(\theta)` gate class"""
    gate_name = 'RZZ'
    gate_name_latex = r'\text{RZZ}'

    def __new__(cls, theta, target1, target2):
        """todo"""
        params = (theta,)
        qubits = (target1, target2)
        return super().__new__(cls, params=params, qubits=qubits)

    def __init__(self, theta, target1, target2):
        """todo"""
        self.params = (theta,)
        self.qubits = (target1, target2)

    def _sympy_matrix(self):
        """todo"""
        theta, = self.get_params_expr()
        plusexp = exp(I * theta/2)
        minusexp = exp(-I * theta/2)
        Matrix([[minusexp, 0, 0, 0],
                [0, plusexp, 0, 0],
                [0, 0, plusexp, 0],
                [0, 0, 0, minusexp]])

    def _represent_ZGate(self, basis, **options):
        """todo"""
        theta, = self.get_params_expr()
        nqubits = options.get('nqubits', self.min_qubits)
        plusexp = exp(I * theta/2)
        minusexp = exp(-I * theta/2)
        coeff_ops = [(minusexp, (op00, op00)),
                     (plusexp, (op11, op00)),
                     (plusexp, (op00, op11)),
                     (minusexp, (op11, op11))]
        matrix = self._define_matrix(coeff_ops=coeff_ops, nqubits=nqubits)
        return matrix
