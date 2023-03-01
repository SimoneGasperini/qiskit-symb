"""Symbolic gate module"""

from sympy import sympify, matrix2numpy
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
        from .controlledgate import ControlledGate
        from .utils import get_init
        gate = circuit_instruction.operation
        if isinstance(gate, QiskitCGate):
            return ControlledGate.get(circuit_instruction)
        return get_init(gate.name)(*gate.params)

    @property
    def sympy_symbols(self):
        """todo"""
        # pylint: disable=protected-access
        return list(dict.fromkeys([sympify(s) for par in self.params
                                   for _, s in par._parameter_symbols.items()]))

    @property
    def sympy_expressions(self):
        """todo"""
        # pylint: disable=protected-access
        return [sympify(par._symbol_expr) for par in self.params]

    def to_sympy(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=no-member
        from .utils import symbols2real
        sympy_matrix = self.__sympy__()
        return symbols2real(sympy_matrix)

    def to_numpy(self, *vals):
        """todo"""
        # pylint: disable=no-member
        args_dict = dict(zip(self.sympy_symbols, vals))
        sympy_matrix = self.__sympy__().subs(args_dict)
        try:
            return matrix2numpy(sympy_matrix, dtype=complex)
        except TypeError:
            return matrix2numpy(sympy_matrix, dtype=object)
