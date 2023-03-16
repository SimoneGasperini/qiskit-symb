"""Symbolic quantum operator module"""

import math
from sympy import matrix2numpy, exp, I
from sympy.physics.quantum import TensorProduct
from qiskit.quantum_info import Operator as qiskit_Operator
from .quantumbase import QuantumBase


class Operator(QuantumBase):
    """Symbolic quantum operator class"""

    def __init__(self, data):
        """todo"""
        super().__init__(data=data)

    @staticmethod
    def _init_from_label(label):
        """todo"""
        return qiskit_Operator.from_label(label).data

    @staticmethod
    def _init_from_circuit(circuit):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from ..utils import flatten_circuit, transpile_circuit
        circuit = transpile_circuit(flatten_circuit(circuit))
        gph = exp(I * circuit.global_phase)
        circ_data = QuantumBase._get_circ_data(circuit)
        return gph * math.prod(TensorProduct(*[gate.to_sympy() for gate in layer[::-1]
                                               if gate is not None]) for layer in circ_data[::-1])

    def to_numpy(self):
        """todo"""
        try:
            return matrix2numpy(self.to_sympy(), dtype=complex)
        except TypeError:
            return matrix2numpy(self.to_sympy(), dtype=object)

    def dot(self, other):
        """todo"""
        if not isinstance(other, Operator):
            other = Operator(other)
        dotprod = self.to_sympy() @ other.to_sympy()
        return self.__class__(dotprod)
