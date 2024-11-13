r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate module"""

from sympy import Matrix, I, Pow, Rational
from ...gate import op00, op01, op10, op11
from ...standardgate import StandardGate


class ECRGate(StandardGate):
    r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate class"""
    gate_name = 'ECR'
    gate_name_latex = r'\text{ECR}'

    def __new__(cls, target1, target2):
        """todo"""
        qubits = (target1, target2)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)

    def __init__(self, target1, target2):
        """todo"""
        self.params = ()
        self.qubits = (target1, target2)

    @staticmethod
    def _sympy_matrix():
        """todo"""
        sqrt2_inv = Pow(2, Rational(-1, 2), evaluate=False)
        return sqrt2_inv * Matrix([[0, 1, 0, I],
                                   [1, 0, -I, 0],
                                   [0, I, 0, 1],
                                   [-I, 0, 1, 0]])

    def _represent_ZGate(self, basis, **options):
        """todo"""
        nqubits = options.get('nqubits', self.min_qubits)
        coeff_ops = [(1, (op01, op00)),
                     (1, (op10, op00)),
                     (I, (op01, op01)),
                     (-I, (op10, op01)),
                     (I, (op01, op10)),
                     (-I, (op10, op10)),
                     (1, (op01, op11)),
                     (1, (op10, op11))]
        sqrt2_inv = Pow(2, Rational(-1, 2), evaluate=False)
        matrix = sqrt2_inv * \
            self._define_matrix(coeff_ops=coeff_ops, nqubits=nqubits)
        return matrix
