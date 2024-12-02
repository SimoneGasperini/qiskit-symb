r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class ECRGate(StandardGate):
    r"""Symbolic Echoed Cross-Resonance :math:`ECR` gate class"""

    def __init__(self, qubit1, qubit2):
        """todo"""
        params = ()
        qubits = (qubit1, qubit2)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        x = 1 / 2**0.5
        return Array([[0, 0, x, x*1j],
                      [0, 0, x*1j, x],
                      [x, -x*1j, 0, 0],
                      [-x*1j, x, 0, 0]])
