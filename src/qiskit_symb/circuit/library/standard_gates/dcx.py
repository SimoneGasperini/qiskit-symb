r"""Symbolic Double-CNOT :math:`DCX` gate module"""

from sympy.matrices import Matrix
from ...gate import Gate


class DCXGate(Gate):
    r"""Symbolic Double-CNOT :math:`DCX` gate class"""

    def __init__(self, qubits=None):
        """todo"""
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='dcx', num_qubits=2, params=[], qubits=qubits)

    def __sympy__(self):
        """todo"""
        return Matrix([[1, 0, 0, 0],
                       [0, 0, 0, 1],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0]])
