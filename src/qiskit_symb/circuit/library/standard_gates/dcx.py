r"""Symbolic Double-CNOT :math:`DCX` gate module"""

from sympy.matrices import Matrix
from ...gate import Gate


class DCXGate(Gate):
    r"""Symbolic Double-CNOT :math:`DCX` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='dcx', num_qubits=2, params=[])

    def __sympy__(self):
        """todo"""
        return Matrix([[1, 0, 0, 0],
                       [0, 0, 0, 1],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0]])
