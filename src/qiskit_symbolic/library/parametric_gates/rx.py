r"""Symbolic :math:`RX(\theta)` gate module"""

import sympy
from sympy.matrices import Matrix
from qiskit_symbolic.gate import Gate


class RXGate(Gate):
    r"""Symbolic :math:`RX(\theta)` gate class"""

    def __init__(self, theta):
        """todo"""
        params = [theta]
        super().__init__(name='rx', num_qubits=1, params=params)

    def __sympy__(self):
        """todo"""
        theta, = self.get_sympy_params()
        i = sympy.I
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        return Matrix([[cos, -i * sin],
                       [-i * sin, cos]])
