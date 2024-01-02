"""Symbolic generic unitary gate module"""

import numpy as np
from sympy.matrices import Matrix
from ...gate import Gate


class UnitaryGate(Gate):
    r"""Symbolic generic unitary gate class"""

    def __init__(self, matrix):
        """todo"""
        num_qubits = int(np.log2(len(matrix)))
        qubits = list(range(num_qubits))
        super().__init__(name='unitary', num_qubits=num_qubits, params=[], qubits=qubits)
        self.matrix = matrix

    def __sympy__(self):
        """todo"""
        return Matrix(self.matrix)
