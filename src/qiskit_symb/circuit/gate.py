"""Symbolic gate module"""

from sympy import sympify
from sympy.physics.quantum import represent
from qiskit.circuit.controlledgate import ControlledGate as QiskitCGate
from sympy.physics.quantum.gate import Gate as SympyGate


class Gate(SympyGate):
    """Symbolic gate abstract class"""

    def __new__(cls, qubits, params):
        """todo"""
        instance = super().__new__(cls, *qubits)
        instance.qubits = qubits
        instance.params = params
        return instance

    @staticmethod
    def get(gate_node):
        """todo"""
        if isinstance(gate_node.op, QiskitCGate):
            name = 'c' + gate_node.op.base_gate.name
        else:
            name = gate_node.op.name
        params = gate_node.op.params
        qubits = (qarg._index for qarg in gate_node.qargs)
        try:
            from . import name2init
            __init__ = name2init[name]
        except KeyError:
            raise NotImplementedError(
                f'Instruction "{name}" is not implemented in qiskit-symb')
        return __init__(*params, *qubits)

    @property
    def nqubits(self):
        """todo"""
        return len(self.qubits)

    @property
    def qubits_label(self):
        return ','.join(str(s) for s in self.label)

    @property
    def params_label(self):
        return ','.join(str(s) for s in self.params[:3])

    def get_params_expr(self):
        """todo"""
        params_expr = tuple(sympify(par._symbol_expr)
                            if hasattr(par, '_symbol_expr') else par
                            for par in self.params)
        return params_expr

    def get_target_matrix(self, format='sympy'):
        """todo"""
        return self.sympy_matrix

    def get_sympy_repr(self, nqubits):
        """todo"""
        return represent(self, nqubits=nqubits)

    def _latex(self, printer, *args):
        """todo"""
        latex_repr = '%s_{%s}' % (self.gate_name_latex, self.qubits_label)
        if self.params:
            latex_repr += '(%s)' % self.params_label
        return latex_repr
