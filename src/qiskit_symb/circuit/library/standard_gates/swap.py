r"""Symbolic :math:`SWAP` and controlled-:math:`SWAP` gates module"""

from sympy import Matrix
from ...gate import op00, op01, op10, op11
from ...standardgate import StandardGate


class SwapGate(StandardGate):
    r"""Symbolic :math:`SWAP` gate class"""
    gate_name = 'SWAP'
    gate_name_latex = r'\text{SWAP}'

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
                       [0, 0, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]])

    def _represent_ZGate(self, basis, **options):
        """todo"""
        nqubits = options.get('nqubits', self.min_qubits)
        coeff_ops = [(1, (op00, op00)),
                     (1, (op01, op10)),
                     (1, (op10, op01)),
                     (1, (op11, op11))]
        matrix = self._define_matrix(coeff_ops=coeff_ops, nqubits=nqubits)
        return matrix
