"""Symbolic quantum operator module"""

import math
import sympy
from sympy.matrices import Matrix, matrix2numpy
from sympy.physics.quantum import TensorProduct
from qiskit.quantum_info import Operator as qiskit_Operator
from .quantumbase import QuantumBase


class Operator(QuantumBase):
    """Symbolic quantum operator class"""

    def __init__(self, data, params):
        """todo"""
        super().__init__(data=data, params=params)

    @staticmethod
    def _get_data_from_label(label):
        """todo"""
        return Matrix(qiskit_Operator.from_label(label).data)

    @staticmethod
    def _get_data_from_circuit(circuit):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        # pylint: disable=too-many-locals
        from ..utils import flatten_circuit, transpile_circuit, get_layers_data
        from ..circuit import Gate, ControlledGate
        from ..circuit.library import IGate
        circuit = transpile_circuit(flatten_circuit(circuit))
        layers_data = get_layers_data(circuit)
        num_qubits, num_layers = circuit.num_qubits, len(layers_data)
        circ_data = [[IGate()] * num_qubits for _ in range(num_layers)]
        for layer_idx in range(num_layers):
            for instruction in layers_data[layer_idx]:
                gate = Gate.get(instruction)
                if isinstance(gate, ControlledGate):
                    gate_span = gate._span
                    qubit_idx = gate_span[0]
                    for i in gate_span[1:]:
                        circ_data[layer_idx][i] = None
                else:
                    qubit_idx = instruction.qargs[0]._index
                circ_data[layer_idx][qubit_idx] = gate
        gph = sympy.exp(sympy.I * circuit.global_phase)
        return gph * math.prod(TensorProduct(*[gate.to_sympy() for gate in layer[::-1]
                                               if gate is not None]) for layer in circ_data[::-1])

    def to_numpy(self):
        """todo"""
        try:
            return matrix2numpy(self.to_sympy(), dtype=complex)
        except TypeError:
            return matrix2numpy(self.to_sympy(), dtype=object)
