r"""Symbolic Pauli :math:`Z` gate module"""

from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class ZGate(Gate):
    r"""Symbolic Pauli :math:`Z` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='z', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        return Matrix([[1, 0],
                       [0, -1]])
