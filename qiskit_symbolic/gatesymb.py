"""Symbolic gate module"""

from sympy.matrices import Matrix


class GateSymb:
    """Symbolic gate class"""

    @staticmethod
    def from_instruction(instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from qiskit_symbolic.utils import get_init
        gate = instruction.operation
        init = get_init(gate.name)
        return init(*gate.params, qubits=instruction.qubits, label=gate.label)

    def get_sympy_params(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=no-member
        from qiskit_symbolic.utils import sympify
        return [sympify(par) for par in self.params]

    def to_sympy(self):
        """todo"""
        # pylint: disable=no-member
        if self.is_parameterized():
            return self.__sympy__()
        return Matrix(self.to_matrix())
