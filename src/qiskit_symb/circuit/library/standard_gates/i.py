r"""Symbolic Pauli :math:`I` gate module"""

from sympy.matrices import Matrix
from ...gate import Gate


class IGate(Gate):
    r"""Symbolic Pauli :math:`I` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='id', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        return Matrix([[1, 0],
                       [0, 1]])
