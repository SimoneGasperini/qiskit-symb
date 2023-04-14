"""Symbolic controlled gate module"""

import sympy
from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from .gate import Gate


class ControlledGate(Gate):
    """Symbolic controlled gate base class"""

    def __init__(self, name, num_qubits, params,
                 ctrl_qubits, target_qubits, ctrl_state, base_gate):
        """todo"""
        # pylint: disable=too-many-arguments
        self.ctrl_qubits = [0] if ctrl_qubits is None else ctrl_qubits
        self.target_qubits = [1] if target_qubits is None else target_qubits
        self.ctrl_state = '1' * len(self.ctrl_qubits) \
            if ctrl_state is None else ctrl_state
        self.base_gate = base_gate
        qubits = self.ctrl_qubits + self.target_qubits
        num_qubits = len(qubits)
        super().__init__(name=name, num_qubits=num_qubits, params=params, qubits=qubits)

    @staticmethod
    def get(instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ..utils import get_init
        gate = instruction.op
        qargs = instruction.qargs
        num_ctrls = gate.num_ctrl_qubits
        ctrl_qubits = [qarg._index for qarg in qargs[:num_ctrls]]
        target_qubits = [qarg._index for qarg in qargs[num_ctrls:]]
        ctrl_state = format(gate.ctrl_state, 'b').zfill(num_ctrls)
        return get_init(gate.name)(*gate.params, ctrl_qubits=ctrl_qubits,
                                   target_qubits=target_qubits, ctrl_state=ctrl_state)

    def __sympy__(self):
        """todo"""
        # pylint: disable=no-member
        imin = min(self.qubits)
        ctrl_qubits = [qbit - imin for qbit in self.ctrl_qubits]
        target_qubits = [qbit - imin for qbit in self.target_qubits]
        igate = Matrix([[1, 0], [0, 1]])
        projector = {'0': Matrix([[1, 0], [0, 0]]),
                     '1': Matrix([[0, 0], [0, 1]])}
        num_ctrls = len(self.ctrl_qubits)
        size = self._size
        terms = []
        for state in range(2**num_ctrls):
            term = [igate] * size
            bitstring = format(state, 'b').zfill(num_ctrls)
            for bit, qbit in zip(bitstring[::-1], ctrl_qubits):
                term[qbit] = projector[bit]
            if bitstring == self.ctrl_state:
                term[target_qubits[0]] = self.base_gate.__sympy__()
                for i in target_qubits[1:]:
                    del term[i]
            terms.append(term)
        return sum((TensorProduct(*term[::-1]) for term in terms),
                   sympy.zeros(2**size))
