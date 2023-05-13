"""Symbolic quantum density matrix module"""

from sympy.matrices import Matrix
from qiskit.quantum_info import DensityMatrix as qiskit_DensityMatrix
from .quantumbase import QuantumBase
from .operator import Operator


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
        # pylint: disable=protected-access
        rho = DensityMatrix._get_data_from_label('0' * circuit.num_qubits)
        mat = Operator._get_data_from_circuit(circuit)
        return mat * rho * mat.T.conjugate()
