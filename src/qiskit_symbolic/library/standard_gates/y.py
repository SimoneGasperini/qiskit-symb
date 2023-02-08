r"""Symbolic Pauli :math:`Y` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class YGate(Gate):
    r"""Symbolic Pauli :math:`Y` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='y', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[0, -i],
                       [i, 0]])
