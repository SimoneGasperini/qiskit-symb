"""Symbolic controlled gate module"""

from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit_symbolic.gate import Gate


class ControlledGate(Gate):
    """Symbolic controlled gate base class"""

    def __init__(self, name, num_qubits, params, ctrl_qubit, tg_qubit, base_gate):
        """todo"""
        # pylint: disable=too-many-arguments
        super().__init__(name=name, num_qubits=num_qubits, params=params)
        self.ctrl_qubit = ctrl_qubit
        self.tg_qubit = tg_qubit
        self.base_gate = base_gate

    @staticmethod
    def get(circuit_instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from qiskit_symbolic.utils import get_init
        ctrl_qubit = circuit_instruction.qubits[0]
        tg_qubit = circuit_instruction.qubits[1]
        gate = circuit_instruction.operation
        return get_init(gate.name)(*gate.params, ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit)

    def to_sympy(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        # pylint: disable=no-member
        from .library.standard_gates import IGate
        control, target = self.ctrl_qubit._index, self.tg_qubit._index
        imin = min(control, target)
        span = abs(control - target) + 1
        zero_term = [IGate().to_sympy()] * span
        zero_term[control - imin] = Matrix([[1, 0], [0, 0]])
        one_term = [IGate().to_sympy()] * span
        one_term[control - imin] = Matrix([[0, 0], [0, 1]])
        one_term[target - imin] = self.base_gate.to_sympy()
        return TensorProduct(*zero_term[::-1]) + TensorProduct(*one_term[::-1])
