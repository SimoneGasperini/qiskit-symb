"""Symbolic quantum operator module"""

from qiskit.quantum_info import Operator as qiskit_Operator
from sympy.matrices import Matrix
from .quantumbase import QuantumBase


class Operator(QuantumBase):
    """Symbolic quantum operator class"""

    def __init__(self, data, params=None):
        """todo"""
        super().__init__(data=data, params=params)

    @staticmethod
    def _get_data_from_label(label):
        """todo"""
        return Matrix(qiskit_Operator.from_label(label).data)

    @staticmethod
    def _get_data_from_circuit(circuit):
        """todo"""
        return QuantumBase._get_circ_unitary(circuit)
