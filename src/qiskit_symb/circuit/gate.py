"""Symbolic gate module"""

from sympy import Matrix, eye, zeros, sympify
from sympy.physics.quantum.matrixutils import matrix_tensor_product
from sympy.physics.quantum.gate import Gate as SympyGate


op00 = Matrix([[1, 0], [0, 0]])  # |0><0|
op01 = Matrix([[0, 1], [0, 0]])  # |0><1|
op10 = Matrix([[0, 0], [1, 0]])  # |1><0|
op11 = Matrix([[0, 0], [0, 1]])  # |1><1|


class Gate(SympyGate):
    """Symbolic gate abstract class"""

    def __new__(cls, params, qubits):
        """todo"""
        symbols = Gate.get_symbols(params=params)
        return super().__new__(cls, *symbols, *qubits)

    @property
    def nqubits(self):
        """todo"""
        return len(self.qubits)

    @property
    def label(self):
        """todo"""
        return super().label[-self.nqubits:]

    @staticmethod
    def get_symbols(params):
        """todo"""
        symbols = set()
        for param in params:
            if hasattr(param, '_symbol_expr'):
                symbols.update(param._symbol_expr.free_symbols)
        symbols = sorted(symbols, key=lambda s: s.name)
        return symbols

    @staticmethod
    def get(gate_node):
        """todo"""
        from . import get_class
        _class = get_class(op=gate_node.op)
        params = gate_node.op.params
        qubits = (qarg._index for qarg in gate_node.qargs)
        return _class(*params, *qubits)

    def _define_matrix(self, coeff_ops, nqubits):
        """todo"""
        matrix = sum((coeff * matrix_tensor_product(
            *(ops[0] if i == nqubits - self.targets[0] - 1 else
              ops[1] if i == nqubits - self.targets[1] - 1 else
              eye(2) for i in range(nqubits)))
            for coeff, ops in coeff_ops),
            start=zeros(2**nqubits))
        return matrix

    def get_params_expr(self):
        """todo"""
        params_expr = tuple(sympify(par._symbol_expr)
                            if hasattr(par, '_symbol_expr') else par
                            for par in self.params)
        return params_expr

    def get_target_matrix(self, format='sympy'):
        """todo"""
        return self._sympy_matrix()

    def _latex(self, printer, *args):
        """todo"""
        controls = getattr(self, 'controls', ())
        qubits_label = ','.join(str(s) for s in controls + self.targets)
        params_label = ','.join(str(s) for s in self.params[:3])
        latex_repr = '%s_{%s}' % (self.gate_name_latex, qubits_label)
        if self.params:
            latex_repr += f'({params_label})'
        return latex_repr
