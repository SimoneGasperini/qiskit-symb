r"""Symbolic :math:`iSWAP` and controlled-:math:`iSWAP` gates module"""

from sympy import Matrix, I
from ...gate import op00, op01, op10, op11
from ...standardgate import StandardGate


class iSwapGate(StandardGate):
    r"""Symbolic :math:`iSWAP` gate class"""
    gate_name = 'iSWAP'
    gate_name_latex = r'\text{iSWAP}'

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
        return Matrix([[1, 0, 0, 0],
                       [0, 0, I, 0],
                       [0, I, 0, 0],
                       [0, 0, 0, 1]])

    def _represent_ZGate(self, basis, **options):
        """todo"""
        nqubits = options.get('nqubits', self.min_qubits)
        coeff_ops = [(1, (op00, op00)),
                     (I, (op01, op10)),
                     (I, (op10, op01)),
                     (1, (op11, op11))]
        matrix = self._define_matrix(coeff_ops=coeff_ops, nqubits=nqubits)
        return matrix
