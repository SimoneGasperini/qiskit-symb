"""Symbolic gate module"""

from sympy import Symbol, sympify, matrix2numpy
from sympy.physics.quantum.gate import Gate as SympyGate
from qiskit.circuit import ControlledGate as QiskitControlledGate


class Gate(SympyGate):
    """Symbolic gate abstract class"""

    def __new__(cls, *qubits, params):
        """todo"""
        instance = super().__new__(cls, *qubits)
        instance.params = params
        return instance

    def get_params_expr(self):
        """todo"""
        params_expr = tuple(sympify(par._symbol_expr)
                            if hasattr(par, '_symbol_expr') else par
                            for par in self.params)
        return params_expr

    def get_target_matrix(self, format='sympy'):
        """todo"""
        if format != 'sympy':
            raise NotImplementedError
        target_matrix = self.to_sympy()
        return target_matrix

    def to_sympy(self):
        """todo"""
        expr = self.sympy_matrix
        symbs = expr.free_symbols
        symb2real = {symb: Symbol(symb.name, real=True) for symb in symbs}
        sympy_matrix = expr.subs(symb2real)
        return sympy_matrix


class StandardGate(Gate):
    """Symbolic standard gate abstract class"""

    def __new__(cls, *qubits):
        return super().__new__(cls, *qubits, params=())

    def to_numpy(self):
        """todo"""
        matrix = self.sympy_matrix
        numpy_matrix = matrix2numpy(matrix, dtype=complex)
        return numpy_matrix


class ParametricGate(Gate):
    """Symbolic parametric gate abstract class"""

    def __new__(cls, *qubits, params):
        return super().__new__(cls, *qubits, params=params)

    def to_numpy(self, par2val):
        symb2val = {Symbol(par.name): val for par, val in par2val.items()}
        matrix = self.sympy_matrix.subs(symb2val)
        numpy_matrix = matrix2numpy(matrix, dtype=complex)
        return numpy_matrix


######################################################################################
######################################################################################
######################################################################################


class oldGate:
    """Symbolic gate base class"""

    def __init__(self, name, num_qubits, params):
        """todo"""
        self.name = name
        self.num_qubits = num_qubits
        self.params = params

    @staticmethod
    def get(instruction):
        """todo"""
        from .controlledgate import ControlledGate
        from ..utils import get_init
        gate = instruction.op
        if isinstance(gate, QiskitControlledGate):
            return ControlledGate.get(instruction)
        return get_init(gate.name)(*gate.params)
