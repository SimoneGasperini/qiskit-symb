r"""Symbolic :math:`T` and :math:`T^{\dagger}` gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class TGate(Gate):
    r"""Symbolic :math:`T` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='t', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0],
                       [0, (1 + i) / sympy.sqrt(2)]])


class TdgGate(Gate):
    r"""Symbolic :math:`T^{\dagger}` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='tdg', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        i = sympy.I
        return Matrix([[1, 0],
                       [0, (1 - i) / sympy.sqrt(2)]])
