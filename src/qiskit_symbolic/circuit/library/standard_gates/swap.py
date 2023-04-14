r"""Symbolic :math:`SWAP` and :math:`CSWAP` gates module"""

from sympy.physics.quantum import TensorProduct
from ...gate import Gate


class SwapGate(Gate):
    r"""Symbolic :math:`SWAP` gate class"""

    def __init__(self, qubits):
        """todo"""
        super().__init__(name='swap', num_qubits=2, params=[], qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from ...library import IGate, XGate, YGate, ZGate
        qubits = [qbit - min(self.qubits) for qbit in self.qubits]
        igate = IGate().to_sympy()
        size = self._size
        term0 = [igate] * size
        term1 = [XGate().to_sympy() if i in qubits else igate for i in range(size)]
        term2 = [YGate().to_sympy() if i in qubits else igate for i in range(size)]
        term3 = [ZGate().to_sympy() if i in qubits else igate for i in range(size)]
        return 1/2 * (TensorProduct(*term0[::-1]) + TensorProduct(*term1[::-1]) +
                      TensorProduct(*term2[::-1]) + TensorProduct(*term3[::-1]))
