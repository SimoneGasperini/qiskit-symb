r"""Symbolic :math:`P(\lambda)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class PhaseGate(Gate):
    r"""Symbolic :math:`P(\lambda)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='p', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        lam, = self.get_sympy_params()
        i = sympy.I
        return Matrix([[1, 0],
                       [0, sympy.exp(i * lam)]])
