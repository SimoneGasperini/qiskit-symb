"""Symbolic quantum statevector module"""

from qiskit.quantum_info import Statevector as qiskit_Statevector
from sympy.matrices import Matrix
from .quantumbase import QuantumBase


class Statevector(QuantumBase):
    """Symbolic quantum statevector class"""

    def __init__(self, data, params=None):
        """todo"""
        super().__init__(data=data, params=params)

    @staticmethod
    def _get_data_from_label(label):
        """todo"""
        return Matrix(qiskit_Statevector.from_label(label).data)

    @staticmethod
    def _get_data_from_circuit(circuit):
        """todo"""
        psi = Statevector._get_data_from_label('0' * circuit.num_qubits)
        unitary = QuantumBase._get_circ_unitary(circuit)
        return unitary * psi
