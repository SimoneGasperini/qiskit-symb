"""Symbolic quantum operator module"""
import copy

import numpy as np
from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct

from qiskit.providers.basicaer.basicaertools import einsum_matmul_index
from qiskit.quantum_info import Operator as qiskit_Operator
from .quantumbase import QuantumBase
from ..circuit import ControlledGate


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
        circ_qubits = circuit.num_qubits

        gph, circ_data = QuantumBase._get_circ_data(circuit=circuit)
        _unitary = np.eye(2**circuit.num_qubits, dtype=complex)
        _unitary = np.reshape(_unitary, circuit.num_qubits * [2, 2])

        skipped_operations = ['measure', "delay", 'barrier', 'reset', 'global_phase']
        for layer in circ_data:
            for gate in layer[::-1]:
                if gate is not None and gate.name not in skipped_operations:
                    gate_qubits = gate.qubits if gate.qubits is not None else [0]
                    g = copy.deepcopy(gate)
                    g.qubits = list(range(gate.num_qubits))
                    if isinstance(g, ControlledGate):
                        g.ctrl_qubits = list(range(gate.num_qubits-len(gate.target_qubits)))
                        tqs = list(range(gate.num_qubits-len(gate.target_qubits), gate.num_qubits))
                        g.target_qubits = tqs
                        g.base_gate.qubits = tqs
                    indexes = einsum_matmul_index(gate_qubits, circ_qubits)
                    gate_tensor = np.reshape(np.array(g.to_sympy(), dtype=np.dtype('O')), len(gate_qubits) * [2, 2])
                    _unitary = np.einsum(indexes, gate_tensor, _unitary, dtype=np.dtype('O'), casting="no", optimize="optimal")
                    g.to_sympy()

        _unitary = np.reshape(_unitary, 2 * [2 ** circuit.num_qubits])
        _unitary = Matrix(_unitary)
        return gph * _unitary
