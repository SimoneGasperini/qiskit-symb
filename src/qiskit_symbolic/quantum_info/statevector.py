"""Symbolic quantum statevector module"""

from sympy.matrices import Matrix, matrix2numpy
from qiskit.quantum_info import Statevector as qiskit_Statevector
from .quantumbase import QuantumBase
from .operator import Operator


class Statevector(QuantumBase):
    """Symbolic quantum statevector class"""

    def __init__(self, data, params):
        """todo"""
        super().__init__(data=data, params=params)

    @staticmethod
    def _get_data_from_label(label):
        """todo"""
        return Matrix(qiskit_Statevector.from_label(label).data)

    @staticmethod
    def _get_data_from_circuit(circuit):
        """todo"""
        # pylint: disable=protected-access
        psi = Statevector._get_data_from_label('0' * circuit.num_qubits)
        mat = Operator._get_data_from_circuit(circuit)
        return mat * psi

    def to_numpy(self):
        """todo"""
        try:
            return matrix2numpy(self.to_sympy(), dtype=complex)[:, 0]
        except TypeError:
            return matrix2numpy(self.to_sympy(), dtype=object)[:, 0]
