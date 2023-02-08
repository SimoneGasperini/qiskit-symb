r"""Symbolic :math:`RZ(\lambda)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class RZGate(Gate):
    r"""Symbolic :math:`RZ(\lambda)` gate class"""

    def __init__(self, phi):
        """todo"""
        params = [phi]
        super().__init__(name='rz', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        lam, = self.get_sympy_params()
        i = sympy.I
        return Matrix([[sympy.exp(-i * lam/2), 0],
                       [0, sympy.exp(i * lam/2)]])
