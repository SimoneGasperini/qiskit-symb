"""Symbolic generic unitary gate module"""

import numpy
from sympy.matrices import Matrix
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from ...gate import Gate


class UnitaryGate(Gate):
    """Symbolic generic unitary gate class"""

    def __init__(self, matrix, qubits=None):
        """todo"""
        num_qubits = int(numpy.log2(len(matrix)))
        qubits = list(range(num_qubits)) if qubits is None else qubits
        super().__init__(name='unitary', num_qubits=num_qubits, params=[], qubits=qubits)
        self.matrix = matrix

    def __sympy__(self):
        """todo"""
        qubits = [qbit - min(self.qubits) for qbit in self.qubits]
        circuit = QuantumCircuit(max(qubits) + 1)
        circuit.unitary(self.matrix, qubits=qubits)
        return Matrix(Operator(circuit).data)
