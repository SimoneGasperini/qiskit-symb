"""Symbolic quantum operator module"""
import copy
from string import ascii_uppercase

import numpy as np
from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct

from qiskit import QuantumCircuit
from qiskit.converters import circuit_to_dag
from qiskit.providers.basicaer import UnitarySimulatorPy
from qiskit.providers.basicaer.basicaertools import _einsum_matmul_index_helper
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

    @staticmethod
    def _get_symbolic_circuit_unitary(circuit):
        #QuantumCircuit
        #dag = circuit_to_dag(circuit)
        circ_qubits = circuit.num_qubits

        gph, circ_data = QuantumBase._get_circ_data(circuit=circuit)
        _unitary = np.eye(2**circuit.num_qubits)
        skipped_operations = ['measure', "delay", 'barrier', 'reset', 'global_phase']
        for layer in circ_data:
            for gate in layer[::-1]:
                if gate is not None and gate.name not in skipped_operations:
                    gate_qubits = gate.qubits if gate.qubits is not None else [0]
                    g = copy.deepcopy(gate)
                    g.qubits = list(range(gate.num_qubits))

                    indexes = einsum_matmul_index(gate_qubits, circ_qubits)
                    gate_tensor = np.reshape(np.array(g.to_sympy(), dtype=np.dtype('O')), len(gate_qubits) * [2, 2])
                    # Apply matrix multiplication
                    # vergleich mit unitary simulator
                    _unitary = np.einsum(indexes, gate_tensor, _unitary, dtype=np.dtype('O'), casting="no", optimize="optimal")
                    g.to_sympy()
        _unitary = Matrix(_unitary)
        return gph * _unitary
def einsum_matmul_index(gate_indices, number_of_qubits):
    """Return the index string for Numpy.einsum matrix-matrix multiplication.

    The returned indices are to perform a matrix multiplication A.B where
    the matrix A is an M-qubit matrix, matrix B is an N-qubit matrix, and
    M <= N, and identity matrices are implied on the subsystems where A has no
    support on B.

    Args:
        gate_indices (list[int]): the indices of the right matrix subsystems
                                   to contract with the left matrix.
        number_of_qubits (int): the total number of qubits for the right matrix.

    Returns:
        str: An indices string for the Numpy.einsum function.
    """

    mat_l, mat_r, tens_lin, tens_lout = _einsum_matmul_index_helper(gate_indices, number_of_qubits)

    # Right indices for the N-qubit input and output tensor
    tens_r = ascii_uppercase[:number_of_qubits]

    # Combine indices into matrix multiplication string format
    # for numpy.einsum function
    return "{mat_l}{mat_r}, ".format(
        mat_l=mat_l, mat_r=mat_r
    ) + "{tens_lin}{tens_r}->{tens_lout}{tens_r}".format(
        tens_lin=tens_lin, tens_lout=tens_lout, tens_r=tens_r
    )
