"""Symbolic gate module"""

import numpy
from sympy import lambdify
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

    def to_matrix(self, _vals=None, dtype=complex):
        """todo"""
        sympy_matrix = self.to_sympy()
        if _vals is None:
            numpy_matrix = numpy.array(sympy_matrix)
        else:
            try:
                numpy_matrix = lambdify(
                    self.params, sympy_matrix, 'numpy')(*_vals)
            except TypeError:
                numpy_matrix = lambdify(
                    self.params, sympy_matrix, 'numpy')(_vals)
        return numpy_matrix.astype(dtype=dtype)
