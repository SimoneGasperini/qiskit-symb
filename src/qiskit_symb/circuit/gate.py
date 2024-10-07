"""Symbolic gate module"""

from sympy import Symbol, sympify, matrix2numpy
from sympy.physics.quantum import represent
from sympy.physics.quantum.gate import Gate as SympyGate
from sympy.physics.quantum.gate import CGate as SympyCGate

from qiskit.circuit import ControlledGate as QiskitControlledGate


class Gate(SympyGate):
    """Symbolic gate abstract class"""

    def __new__(cls, qubits, params):
        """todo"""
        instance = super().__new__(cls, *qubits)
        instance.qubits = qubits
        instance.params = params
        return instance

    @property
    def nqubits(self):
        return len(self.qubits)

    def get_params_expr(self):
        """todo"""
        params_expr = tuple(sympify(par._symbol_expr)
                            if hasattr(par, '_symbol_expr') else par
                            for par in self.params)
        return params_expr

    def get_target_matrix(self, format='sympy'):
        return self.sympy_matrix

    def get_sympy_repr(self, nqubits):
        return represent(self, nqubits=nqubits)


class StandardGate(Gate):
    """Symbolic standard gate abstract class"""

    def get_numpy_repr(self, nqubits):
        """todo"""
        matrix = self.get_sympy_repr(nqubits=nqubits)
        numpy_matrix = matrix2numpy(matrix, dtype=complex)
        return numpy_matrix


class ParametricGate(Gate):
    """Symbolic parametric gate abstract class"""

    def get_numpy_repr(self, nqubits, par2val):
        symb2val = {Symbol(par.name): val for par, val in par2val.items()}
        matrix = self.get_sympy_repr(nqubits=nqubits).subs(symb2val)
        numpy_matrix = matrix2numpy(matrix, dtype=complex)
        return numpy_matrix

    def _latex(self, printer, *args):
        """todo"""
        label = ','.join(str(s) for s in self.label)
        params = ','.join(str(s) for s in self.params[:3])
        return '%s_{%s}(%s)' % (self.gate_name_latex, label, params)


class ControlledGate(Gate, SympyCGate):
    """Symbolic controlled gate abstract class"""
    def __new__(cls, controls, target_gate):
        return SympyCGate.__new__(cls, *controls, target_gate)

    def get_target_matrix(self, format='sympy'):
        """todo"""
        return self.gate.sympy_matrix

    def _latex(self, printer, *args):
        """todo"""
        label = ','.join(str(s) for s in self.controls + self.targets)
        params = ','.join(str(s) for s in self.gate.params[:3])
        return '%s_{%s}(%s)' % (self.gate_name_latex, label, params)


######################################################################################
######################################################################################
######################################################################################


@staticmethod
def get(instruction):
    """todo"""
    from ..utils import get_init
    gate = instruction.op
    if isinstance(gate, QiskitControlledGate):
        return ControlledGate.get(instruction)
    return get_init(gate.name)(*gate.params)


@staticmethod
def get(instruction):
    """todo"""
    from ..utils import get_init
    gate = instruction.op
    name = 'c' + gate.base_gate.name
    num_ctrl_qubits = gate.num_ctrl_qubits
    ctrl_state = format(gate.ctrl_state, 'b').zfill(num_ctrl_qubits)
    return get_init(name)(*gate.params, num_ctrl_qubits=num_ctrl_qubits, ctrl_state=ctrl_state)
