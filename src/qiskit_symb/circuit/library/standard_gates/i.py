r"""Symbolic Pauli :math:`I` gate module"""

from sympy import Matrix
from sympy.physics.quantum.gate import IdentityGate
from ...standardgate import StandardGate


class IGate(StandardGate, IdentityGate):
    r"""Symbolic Pauli math:`I` gate class"""
    gate_name = 'I'
    gate_name_latex = r'\text{I}'

    def __new__(cls, target):
        """todo"""
        qubits = (target,)
        params = ()
        return super().__new__(cls, qubits=qubits, params=params)

    def __init__(self, target):
        """todo"""
        self.params = ()
        self.qubits = (target,)

    @staticmethod
    def _sympy_matrix():
        return Matrix([[1, 0],
                       [0, 1]])
