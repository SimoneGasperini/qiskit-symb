"""Symbolic quantum density matrix module"""

from qiskit.quantum_info import DensityMatrix as qiskit_DensityMatrix
from sympy.matrices import Matrix
from .quantumbase import QuantumBase


class DensityMatrix(QuantumBase):
    """Symbolic quantum density matrix class"""

    def __init__(self, data, params=None):
        """todo"""
        super().__init__(data=data, params=params)

    @staticmethod
    def _get_data_from_label(label):
        """todo"""
        return Matrix(qiskit_DensityMatrix.from_label(label).data)

    @staticmethod
    def _get_data_from_circuit(circuit):
        """todo"""
        rho = DensityMatrix._get_data_from_label('0' * circuit.num_qubits)
        unitary = QuantumBase._get_circ_unitary(circuit)
        return unitary * rho * unitary.transpose().conjugate()
