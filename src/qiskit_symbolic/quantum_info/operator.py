"""Symbolic quantum operator module"""

from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit.quantum_info import Operator as qiskit_Operator
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
        mat = Operator._get_data_from_label('I' * circuit.num_qubits)
        gph, circ_data = QuantumBase._get_circ_data(circuit=circuit)
        for layer in circ_data:
            mat = TensorProduct(*[gate.to_sympy() for gate in layer[::-1]
                                  if gate is not None]) * mat
        return gph * mat
