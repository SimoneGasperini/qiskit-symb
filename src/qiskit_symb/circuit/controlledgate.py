"""Symbolic controlled gate module"""

import numpy
import sympy
from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from .gate import Gate


class ControlledGate(Gate):
    """Symbolic controlled gate base class"""

    def __init__(self, name, num_qubits, params, base_gate, num_ctrl_qubits, ctrl_state):
        """todo"""
        # pylint: disable=too-many-arguments
        super().__init__(name=name, num_qubits=num_qubits, params=params)
        self.base_gate = base_gate
        self.num_ctrl_qubits = num_ctrl_qubits
        self.ctrl_state = '1' * num_ctrl_qubits if ctrl_state is None else ctrl_state

    @staticmethod
    def get(instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from ..utils import get_init
        gate = instruction.op
        name = 'c' + gate.base_gate.name
        num_ctrl_qubits = gate.num_ctrl_qubits
        ctrl_state = format(gate.ctrl_state, 'b').zfill(num_ctrl_qubits)
        return get_init(name)(*gate.params, num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)

    def __sympy__(self):
        """todo"""
        # pylint: disable=no-member
        proj = {'0': Matrix([[1, 0], [0, 0]]),
                '1': Matrix([[0, 0], [0, 1]])}
        sympy_matrix = sympy.zeros(2**self.num_qubits)
        for state in range(2**self.num_ctrl_qubits):
            bitstring = format(state, 'b').zfill(self.num_ctrl_qubits)
            factors = [proj[bit] for bit in bitstring]
            if bitstring == self.ctrl_state:
                matrix = self.base_gate.__sympy__()
                term = TensorProduct(matrix, *factors)
            else:
                identity = Matrix(numpy.eye(2**self.base_gate.num_qubits))
                term = TensorProduct(identity, *factors)
            sympy_matrix += term
        return sympy_matrix
