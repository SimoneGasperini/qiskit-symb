r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class UGate(Gate):
    r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate class"""

    def __init__(self, theta, phi, lam):
        """todo"""
        params = [theta, phi, lam]
        super().__init__(name='u', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, phi, lam = self.get_sympy_params()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        exp = sympy.exp
        return Matrix([[cos, -exp(i * lam) * sin],
                       [exp(i * phi) * sin, exp(i * (phi + lam)) * cos]])
