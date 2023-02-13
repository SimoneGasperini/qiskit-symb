"""Symbolic controlled gate module"""

import sympy
from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit_symbolic.gate import Gate


class ControlledGate(Gate):
    """Symbolic controlled gate base class"""

    def __init__(self, name, num_qubits, params, ctrl_qubit, tg_qubit, base_gate,
                 global_phase=False):
        """todo"""
        # pylint: disable=too-many-arguments
        super().__init__(name=name, num_qubits=num_qubits, params=params)
        self.ctrl_qubit = ctrl_qubit
        self.tg_qubit = tg_qubit
        self.base_gate = base_gate
        self.global_phase = global_phase

    @staticmethod
    def get(circuit_instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from .utils import get_init
        ctrl_qubit = circuit_instruction.qubits[0]._index
        tg_qubit = circuit_instruction.qubits[1]._index
        gate = circuit_instruction.operation
        return get_init(gate.name)(*gate.params, ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit)

    def to_sympy(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=no-member
        from .utils import sympify
        from .library.standard_gates import IGate
        imin = min(self.ctrl_qubit, self.tg_qubit)
        span = abs(self.ctrl_qubit - self.tg_qubit) + 1
        zero_term = [IGate().to_sympy()] * span
        zero_term[self.ctrl_qubit - imin] = Matrix([[1, 0], [0, 0]])
        one_term = [IGate().to_sympy()] * span
        one_term[self.ctrl_qubit - imin] = Matrix([[0, 0], [0, 1]])
        one_term[self.tg_qubit - imin] = self.base_gate.to_sympy()
        gph = 1
        if self.global_phase:
            i = sympy.I
            gamma = sympify(self.params[-1])
            gph = sympy.exp(i * gamma)
        return TensorProduct(*zero_term[::-1]) + gph * TensorProduct(*one_term[::-1])
