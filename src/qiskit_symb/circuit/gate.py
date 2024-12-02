"""Symbolic gate module"""

from sympy import sympify


class Gate:
    """Symbolic gate abstract class"""

    def __init__(self, params, qubits):
        """todo"""
        self.params = params
        self.qubits = qubits

    @property
    def nqubits(self):
        """todo"""
        return len(self.qubits)

    @staticmethod
    def get(gate_node):
        """todo"""
        from . import get_class
        _class = get_class(op=gate_node.op)
        params = gate_node.op.params
        qubits = [qarg._index for qarg in gate_node.qargs]
        return _class(*params, *qubits)

    def _get_params_expr(self):
        """todo"""
        params_expr = [sympify(param._symbol_expr)
                       if hasattr(param, '_symbol_expr') else param
                       for param in self.params]
        return params_expr

    def _get_tensor_array(self):
        """todo"""
        tensor_array = self._sympy_array()
        if self.nqubits > 1:
            shape = (2,) * 2**self.nqubits
            tensor_array = tensor_array.reshape(*shape)
        return tensor_array

    def to_sympy(self):
        """todo"""
        return self._sympy_array()
