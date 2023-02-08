"""Symbolic gate module"""

from qiskit.circuit import ControlledGate as QiskitCGate


class Gate:
    """Symbolic gate base class"""

    def __init__(self, name, num_qubits, params):
        """todo"""
        self.name = name
        self.num_qubits = num_qubits
        self.params = params

    @staticmethod
    def get(circuit_instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=cyclic-import
        from qiskit_symbolic.controlledgate import ControlledGate
        from qiskit_symbolic.utils import get_init
        gate = circuit_instruction.operation
        if isinstance(gate, QiskitCGate):
            return ControlledGate.get(circuit_instruction)
        return get_init(gate.name)(*gate.params)

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
