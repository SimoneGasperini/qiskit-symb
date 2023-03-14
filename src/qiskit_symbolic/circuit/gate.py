"""Symbolic gate module"""

from sympy import matrix2numpy
from qiskit.circuit import ControlledGate as QiskitControlledGate


class Gate:
    """Symbolic gate base class"""

    def __init__(self, name, num_qubits, params):
        """todo"""
        self.name = name
        self.num_qubits = num_qubits
        self.params = params

    @staticmethod
    def get(instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=cyclic-import
        from .controlledgate import ControlledGate
        from ..utils import get_init
        gate = instruction.op
        if isinstance(gate, QiskitControlledGate):
            return ControlledGate.get(instruction)
        return get_init(gate.name)(*gate.params)

    def _get_params_expr(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from ..utils import get_symbolic_expr
        return [get_symbolic_expr(par) for par in self.params]

    def _get_unique_symbols(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from ..utils import get_unique_symbols
        sympy_symbols = []
        for par in self.params:
            sympy_symbols.extend(get_unique_symbols(par))
        return list(dict.fromkeys(sympy_symbols))

    def to_sympy(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=no-member
        from ..utils import symbols2real
        sympy_matrix = self.__sympy__()
        return symbols2real(sympy_matrix)

    def to_numpy(self, *vals):
        """todo"""
        # pylint: disable=no-member
        sympy_symbols = self._get_unique_symbols()
        if len(vals) > len(sympy_symbols):
            raise ValueError
        sympy_matrix = self.__sympy__().subs(dict(zip(sympy_symbols, vals)))
        try:
            return matrix2numpy(sympy_matrix, dtype=complex)
        except TypeError:
            return matrix2numpy(sympy_matrix, dtype=object)
