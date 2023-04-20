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
        self.base_gate.qubits = target_qubits
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
        name = 'c' + gate.base_gate.name
        qargs = instruction.qargs
        num_ctrls = gate.num_ctrl_qubits
        ctrl_qubits = [qarg._index for qarg in qargs[:num_ctrls]]
        target_qubits = [qarg._index for qarg in qargs[num_ctrls:]]
        ctrl_state = format(gate.ctrl_state, 'b').zfill(num_ctrls)
        return get_init(name)(*gate.params, ctrl_qubits=ctrl_qubits,
                              target_qubits=target_qubits, ctrl_state=ctrl_state)

    def __sympy__(self):
        """todo"""
        # pylint: disable=protected-access
        # pylint: disable=no-member
        igate = Matrix([[1, 0], [0, 1]])
        proj = {'0': Matrix([[1, 0], [0, 0]]),
                '1': Matrix([[0, 0], [0, 1]])}
        gate_size = self._size
        ctrl_qubits = [qbit - min(self.qubits) for qbit in self.ctrl_qubits]
        base_span = [qbit - min(self.qubits) for qbit in self.base_gate._span]
        num_ctrls = len(self.ctrl_qubits)
        sympy_matrix = sympy.zeros(2**gate_size)
        for state in range(2**num_ctrls):
            term = [igate] * gate_size
            bitstring = format(state, 'b').zfill(num_ctrls)
            for bit, qbit in zip(bitstring[::-1], ctrl_qubits):
                term[qbit] = proj[bit]
            term = TensorProduct(*term[::-1])
            if bitstring == self.ctrl_state:
                base_term = [igate] * gate_size
                base_term[base_span[0]] = self.base_gate.__sympy__()
                base_term = [gate for qbit, gate in enumerate(base_term)
                             if qbit not in base_span[1:]]
                term *= TensorProduct(*base_term[::-1])
            sympy_matrix += term
        return sympy_matrix
