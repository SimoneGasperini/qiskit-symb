"""Symbolic gate module"""

from sympy import Symbol, sympify


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

    @staticmethod
    def _to_sympy_param(param):
        """todo"""
        if hasattr(param, "parameters") and param.parameters:
            expr = str(param)
            locals_dict = {}
            sorted_params = sorted(
                param.parameters, key=lambda par: len(par.name), reverse=True
            )
            for idx, subparam in enumerate(sorted_params):
                safe_name = f"_p{idx}"
                expr = expr.replace(subparam.name, safe_name)
                locals_dict[safe_name] = Symbol(subparam.name)
            return sympify(expr, locals=locals_dict)
        if hasattr(param, "name"):
            return Symbol(param.name)
        if hasattr(param, "_symbol_expr"):
            return sympify(param._symbol_expr)
        return param

    def _get_params_expr(self):
        """todo"""
        return [self._to_sympy_param(param) for param in self.params]

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
