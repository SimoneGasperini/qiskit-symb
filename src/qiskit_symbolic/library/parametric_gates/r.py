r"""Symbolic :math:`R(\theta, \phi)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class RGate(Gate):
    r"""Symbolic :math:`R(\theta, \phi)` gate class"""

    def __init__(self, theta, phi):
        """todo"""
        params = [theta, phi]
        super().__init__(name='r', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, phi = self.get_sympy_params()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        return Matrix([[cos, -i * sympy.exp(-i * phi) * sin],
                       [-i * sympy.exp(i * phi) * sin, cos]])
