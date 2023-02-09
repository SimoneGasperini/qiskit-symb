r"""Symbolic :math:`S` and :math:`S^{\dagger}` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class SGate(Gate):
    r"""Symbolic :math:`S` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='s', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0],
                       [0, i]])


class SdgGate(Gate):
    r"""Symbolic :math:`S^{\dagger}` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='sdg', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0],
                       [0, -i]])
