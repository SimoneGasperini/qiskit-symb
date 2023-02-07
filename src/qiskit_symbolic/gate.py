"""Symbolic gate module"""

from sympy.matrices import Matrix
from qiskit.circuit import CircuitInstruction, Instruction


class GateSymb:
    """Symbolic gate base class"""

    @staticmethod
    def get(obj):
        """todo"""
        if isinstance(obj, CircuitInstruction):
            return GateSymb.from_circuit_instruction(obj)
        if isinstance(obj, Instruction):
            return GateSymb.from_instruction(obj)
        raise TypeError

    @staticmethod
    def from_circuit_instruction(circuit_instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from qiskit_symbolic.utils import get_init
        instruction = circuit_instruction.operation
        qubits = circuit_instruction.qubits
        init = get_init(instruction.name)
        return init(*instruction.params, qubits=qubits, label=instruction.label)

    @staticmethod
    def from_instruction(instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from qiskit_symbolic.utils import get_init
        init = get_init(instruction.name)
        return init(*instruction.params, label=instruction.label)

    def get_sympy_params(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=no-member
        from qiskit_symbolic.utils import sympify
        return [sympify(par) for par in self.params]

    def to_sympy(self):
        """todo"""
        # pylint: disable=no-member
        if not self.is_parameterized() and len(self.qubits) == 1:
            return Matrix(self.to_matrix())
        return self.__sympy__()
