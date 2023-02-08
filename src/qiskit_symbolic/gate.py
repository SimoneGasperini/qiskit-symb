"""Symbolic gate module"""

from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit.circuit import ControlledGate


class Gate:
    """Symbolic gate base class"""

    def __init__(self, name, num_qubits, params):
        """todo"""
        self.name = name
        self.num_qubits = num_qubits
        self.params = params

    @staticmethod
    def init(circ_instruction):
        """todo"""
        return Gate.from_circ_instruction(circ_instruction)

    @staticmethod
    def from_circ_instruction(circ_instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from qiskit_symbolic.utils import get_init
        instruction = circ_instruction.operation
        name = instruction.name
        params = instruction.params
        if isinstance(instruction, ControlledGate):
            ctrl_qubit = circ_instruction.qubits[0]
            tg_qubit = circ_instruction.qubits[1]
            return get_init(name)(*params, ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit)
        return Gate.from_instruction(instruction)

    @staticmethod
    def from_instruction(instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from qiskit_symbolic.utils import get_init
        name = instruction.name
        params = instruction.params
        return get_init(name)(*params)

    def get_ctrl_unitary(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        # pylint: disable=no-member
        from .library.standard_gates import IGate
        control, target = self.ctrl_qubit._index, self.tg_qubit._index
        imin = min(control, target)
        control, target = control - imin, target - imin
        span = abs(control - target) + 1
        zero_term = [IGate().to_sympy()] * span
        zero_term[control] = Matrix([[1, 0], [0, 0]])
        one_term = [IGate().to_sympy()] * span
        one_term[control] = Matrix([[0, 0], [0, 1]])
        one_term[target] = self.base_gate.to_sympy()
        return TensorProduct(*zero_term[::-1]) + TensorProduct(*one_term[::-1])

    def get_sympy_params(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=no-member
        from qiskit_symbolic.utils import sympify
        return [sympify(par) for par in self.params]

    def to_sympy(self):
        """todo"""
        # pylint: disable=no-member
        return self.__sympy__()
