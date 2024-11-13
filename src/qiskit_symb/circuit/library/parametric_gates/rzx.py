r"""Symbolic :math:`RZX(\theta)` and controlled-:math:`RZX(\theta)` gates module"""

from sympy import Matrix, I, sin, cos
from ...gate import op00, op01, op10, op11
from ...parametricgate import ParametricGate


class RZXGate(ParametricGate):
    r"""Symbolic :math:`RZX(\theta)` gate class"""
    gate_name = 'RZX'
    gate_name_latex = r'\text{RZX}'

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
        costh2 = cos(theta / 2)
        isinth2 = I * sin(theta / 2)
        return Matrix([[costh2, 0, -isinth2, 0],
                       [0, costh2, 0, isinth2],
                       [-isinth2, 0, costh2, 0],
                       [0, isinth2, 0, costh2]])

    def _represent_ZGate(self, basis, **options):
        """todo"""
        theta, = self.get_params_expr()
        nqubits = options.get('nqubits', self.min_qubits)
        costh2 = cos(theta / 2)
        isinth2 = I * sin(theta / 2)
        coeff_ops = [(costh2, (op00, op00)),
                     (costh2, (op11, op00)),
                     (costh2, (op00, op11)),
                     (costh2, (op11, op11)),
                     (-isinth2, (op00, op01)),
                     (isinth2, (op11, op01)),
                     (-isinth2, (op00, op10)),
                     (isinth2, (op11, op10))]
        matrix = self._define_matrix(coeff_ops=coeff_ops, nqubits=nqubits)
        return matrix
