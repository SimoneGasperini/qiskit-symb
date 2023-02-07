"""Symbolic gate module"""

from sympy.matrices import Matrix
from qiskit.circuit import ControlledGate


class GateSymb:
    """Symbolic gate base class"""

    @staticmethod
    def init(circ_instruction):
        """todo"""
        return GateSymb.from_circ_instruction(circ_instruction)

    @staticmethod
    def from_circ_instruction(circ_instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from qiskit_symbolic.utils import get_init
        instruction = circ_instruction.operation
        qubits = circ_instruction.qubits
        name = instruction.name
        params = instruction.params
        label = instruction.label
        if isinstance(instruction, ControlledGate):
            ctrl_qubit, tg_qubit = GateSymb.get_control_target(qubits)
            return get_init(name)(*params, ctrl_qubit=ctrl_qubit, tg_qubit=tg_qubit, label=label)
        return GateSymb.from_instruction(instruction)

    @staticmethod
    def from_instruction(instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from qiskit_symbolic.utils import get_init
        name = instruction.name
        params = instruction.params
        label = instruction.label
        return get_init(name)(*params, label=label)

    @staticmethod
    def get_control_target(qubits):
        """todo"""
        # pylint: disable=protected-access
        control = qubits[0]._index
        target = qubits[1]._index
        i_min = min(control, target)
        return control - i_min, target - i_min

    def get_sympy_params(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=no-member
        from qiskit_symbolic.utils import sympify
        return [sympify(par) for par in self.params]

    def to_sympy(self):
        """todo"""
        # pylint: disable=no-member
        if not self.is_parameterized() and self.num_qubits == 1:
            return Matrix(self.to_matrix())
        return self.__sympy__()
