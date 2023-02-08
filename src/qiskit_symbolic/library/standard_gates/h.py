r"""Symbolic Hadamard :math:`H` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class HGate(Gate):
    r"""Symbolic Hadamard :math:`H` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='h', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        return (1 / sympy.sqrt(2)) * Matrix([[1, 1],
                                             [1, -1]])
