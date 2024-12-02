"""Symbolic gate module"""

from sympy import Matrix, eye, zeros, sympify
from sympy.physics.quantum.matrixutils import matrix_tensor_product


op00 = Matrix([[1, 0], [0, 0]])  # |0><0|
op01 = Matrix([[0, 1], [0, 0]])  # |0><1|
op10 = Matrix([[0, 0], [1, 0]])  # |1><0|
op11 = Matrix([[0, 0], [0, 1]])  # |1><1|


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

    def _define_matrix(self, coeff_ops, nqubits):
        """todo"""
        matrix = sum((coeff * matrix_tensor_product(
            *(ops[0] if i == nqubits - self.targets[0] - 1 else
              ops[1] if i == nqubits - self.targets[1] - 1 else
              eye(2) for i in range(nqubits)))
            for coeff, ops in coeff_ops),
            start=zeros(2**nqubits))
        return matrix

    def to_sympy(self):
        """todo"""
        return self._sympy_array()
