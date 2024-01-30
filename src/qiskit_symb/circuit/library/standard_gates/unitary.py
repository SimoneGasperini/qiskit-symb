"""Symbolic generic unitary gate module"""

import numpy
from sympy.matrices import Matrix
from ...gate import Gate


class UnitaryGate(Gate):
    """Symbolic generic unitary gate class"""

    def __init__(self, matrix):
        """todo"""
        num_qubits = int(numpy.log2(len(matrix)))
        super().__init__(name='unitary', num_qubits=num_qubits, params=[])
        self.matrix = matrix

    def __sympy__(self):
        """todo"""
        return Matrix(self.matrix)
