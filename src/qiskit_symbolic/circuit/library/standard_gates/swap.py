r"""Symbolic :math:`SWAP` and controlled-:math:`SWAP` gates module"""

from sympy.physics.quantum import TensorProduct
from ...gate import Gate
from ...controlledgate import ControlledGate


class SwapGate(Gate):
    r"""Symbolic :math:`SWAP` gate class"""

    def __init__(self, qubits=None):
        """todo"""
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='swap', num_qubits=2, params=[], qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from ...library import IGate, XGate, YGate, ZGate
        qubits = [qbit - min(self.qubits) for qbit in self.qubits]
        igate = IGate().__sympy__()
        size = self._size
        term0 = [igate] * size
        term1 = [XGate().__sympy__() if i in qubits else igate
                 for i in range(size)]
        term2 = [YGate().__sympy__() if i in qubits else igate
                 for i in range(size)]
        term3 = [ZGate().__sympy__() if i in qubits else igate
                 for i in range(size)]
        return 1/2 * (TensorProduct(*term0[::-1]) + TensorProduct(*term1[::-1]) +
                      TensorProduct(*term2[::-1]) + TensorProduct(*term3[::-1]))


class CSwapGate(ControlledGate):
    r"""Symbolic controlled-:math:`SWAP` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = SwapGate(qubits=target_qubits)
        super().__init__(name='cswap', num_qubits=3, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
