r"""Symbolic :math:`iSWAP` gate module"""

import sympy
from sympy.physics.quantum import TensorProduct
from ...gate import Gate


# pylint: disable=invalid-name
# pylint: disable=duplicate-code
class iSwapGate(Gate):
    r"""Symbolic :math:`iSWAP` gate class"""

    def __init__(self, qubits=None):
        """todo"""
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='iswap', num_qubits=2, params=[], qubits=qubits)

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
        i = sympy.I
        return 1/2 * (TensorProduct(*term0[::-1]) + i * TensorProduct(*term1[::-1]) +
                      i * TensorProduct(*term2[::-1]) + TensorProduct(*term3[::-1]))
