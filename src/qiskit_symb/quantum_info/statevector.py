"""Symbolic quantum statevector module"""

from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit.quantum_info import Statevector as qiskit_Statevector
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
        gph, circ_data = QuantumBase._get_circ_data(circuit=circuit)
        for layer in circ_data:
            psi = TensorProduct(*[gate.to_sympy() for gate in layer[::-1]
                                  if gate is not None]) * psi
        return gph * psi
