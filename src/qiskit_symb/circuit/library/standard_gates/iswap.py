r"""Symbolic :math:`iSWAP` and controlled-:math:`iSWAP` gates module"""

import sympy
from sympy.physics.quantum import TensorProduct
from ...gate import Gate
from ...controlledgate import ControlledGate


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
        igate = IGate().__sympy__()
        size = self._size
        term0 = [igate] * size
        term1 = [XGate().__sympy__() if i in qubits else igate
                 for i in range(size)]
        term2 = [YGate().__sympy__() if i in qubits else igate
                 for i in range(size)]
        term3 = [ZGate().__sympy__() if i in qubits else igate
                 for i in range(size)]
        i = sympy.I
        return 1/2 * (TensorProduct(*term0[::-1]) + i * TensorProduct(*term1[::-1]) +
                      i * TensorProduct(*term2[::-1]) + TensorProduct(*term3[::-1]))


class CiSwapGate(ControlledGate):
    r"""Symbolic controlled-:math:`iSWAP` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = iSwapGate(qubits=target_qubits)
        super().__init__(name='ciswap', num_qubits=3, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
