"""Symbolic gate module"""

from sympy import sympify
from sympy.physics.quantum import represent
from sympy.physics.quantum.gate import Gate as SympyGate


class Gate(SympyGate):
    """Symbolic gate abstract class"""

    def __new__(cls, qubits, params):
        """todo"""
        obj = super().__new__(cls, *qubits)
        obj.qubits = qubits
        obj.params = params
        return obj

    @staticmethod
    def get(gate_node):
        """todo"""
        from . import get_class
        _class = get_class(op=gate_node.op)
        params = gate_node.op.params
        qubits = (qarg._index for qarg in gate_node.qargs)
        return _class(*params, *qubits)

    @property
    def nqubits(self):
        """todo"""
        return len(self.qubits)

    @property
    def qubits_label(self):
        """todo"""
        return ','.join(str(s) for s in self.label)

    @property
    def params_label(self):
        """todo"""
        return ','.join(str(s) for s in self.params[:3])

    def get_params_expr(self):
        """todo"""
        params_expr = tuple(sympify(par._symbol_expr)
                            if hasattr(par, '_symbol_expr') else par
                            for par in self.params)
        return params_expr

    def get_target_matrix(self, format='sympy'):
        """todo"""
        return self._sympy_matrix()

    def get_sympy_repr(self, nqubits):
        """todo"""
        return represent(self, nqubits=nqubits)

    def _latex(self, printer, *args):
        """todo"""
        latex_repr = '%s_{%s}' % (self.gate_name_latex, self.qubits_label)
        if self.params:
            latex_repr += '(%s)' % self.params_label
        return latex_repr
