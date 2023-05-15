r"""Symbolic :math:`ECR` and controlled-:math:`ECR` gates module"""

import sympy
from sympy.physics.quantum import TensorProduct
from ...gate import Gate
from ...controlledgate import ControlledGate


class ECRGate(Gate):
    r"""Symbolic :math:`ECR` gate class"""

    def __init__(self, qubits=None):
        """todo"""
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='ecr', num_qubits=2, params=[], qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from ...library import IGate, XGate, YGate
        qubits = [qbit - min(self.qubits) for qbit in self.qubits]
        term0 = [IGate().__sympy__()] * self._size
        term0[qubits[0]] = XGate().__sympy__()
        term1 = [IGate().__sympy__()] * self._size
        term1[qubits[0]] = YGate().__sympy__()
        term1[qubits[1]] = XGate().__sympy__()
        return 1/sympy.sqrt(2) * (TensorProduct(*term0[::-1]) - TensorProduct(*term1[::-1]))


class CECRGate(ControlledGate):
    r"""Symbolic controlled-:math:`ECR` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = ECRGate(qubits=target_qubits)
        super().__init__(name='cecr', num_qubits=3, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
