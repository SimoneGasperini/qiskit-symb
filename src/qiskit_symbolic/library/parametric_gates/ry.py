r"""Symbolic :math:`RY(\theta)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class RYGate(Gate):
    r"""Symbolic :math:`RY(\theta)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='ry', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, = self.get_sympy_params()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        return Matrix([[cos, -sin],
                       [sin, cos]])
