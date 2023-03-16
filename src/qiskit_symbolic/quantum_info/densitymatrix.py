"""Symbolic quantum density matrix module"""

import numpy as np
from sympy import simplify, matrix2numpy
from sympy.physics.quantum import TensorProduct
from qiskit.quantum_info import DensityMatrix as qiskit_DensityMatrix
from .quantumbase import QuantumBase


class DensityMatrix(QuantumBase):
    """Symbolic quantum density matrix class"""

    def __init__(self, data):
        """todo"""
        super().__init__(data=data)

    @staticmethod
    def _init_from_label(label):
        """todo"""
        return qiskit_DensityMatrix.from_label(label).data

    @staticmethod
    def _init_from_circuit(circuit):
        """todo"""
        rho = DensityMatrix.from_label('0' * circuit.num_qubits)
        return rho.evolve(circuit).to_sympy()

    def to_numpy(self):
        """todo"""
        try:
            return matrix2numpy(self.to_sympy(), dtype=complex)
        except TypeError:
            return matrix2numpy(self.to_sympy(), dtype=object)

    def trace(self):
        """todo"""
        return simplify(self.to_sympy().trace())

    def purity(self):
        """todo"""
        return simplify((self.to_sympy() @ self.to_sympy()).trace())

    def is_unit_trace(self):
        """todo"""
        try:
            numpy_matrix = matrix2numpy(self.to_sympy(), dtype=complex)
            return np.allclose(np.trace(numpy_matrix), 1)
        except TypeError:
            return self.trace() == 1

    def is_hermitian(self):
        """todo"""
        return self.to_sympy() == self.dagger().to_sympy()

    def is_positive_semidefinite(self):
        """todo"""
        eigvals = self.to_sympy().eigenvals(
            simplify=True, rational=True, multiple=True)
        for eigval in eigvals:
            if eigval < 0:
                return False
        return True

    def is_valid(self):
        """todo"""
        return self.is_unit_trace() and self.is_hermitian() and self.is_positive_semidefinite()

    def evolve(self, other):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from . import Operator
        if not isinstance(other, Operator):
            operator = Operator(other)
        return self.__class__(operator.dagger().to_sympy() * self.to_sympy() * operator.to_sympy())

    def tensor(self, other):
        """todo"""
        if not isinstance(other, DensityMatrix):
            other = DensityMatrix(other)
        tensorprod = TensorProduct(self.to_sympy(), other.to_sympy())
        return self.__class__(tensorprod)
