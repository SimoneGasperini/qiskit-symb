"""Symbolic quantum operator module"""

import re
import math
from sympy import matrix2numpy, exp, I
from sympy.physics.quantum import TensorProduct
from .quantumbase import QuantumBase
from ..circuit import Gate, ControlledGate
from ..circuit.library import (
    IGate, XGate, YGate, ZGate,
    HGate, SGate, TGate
)


class Operator(QuantumBase):
    """Symbolic quantum operator class"""

    def __init__(self, data):
        """todo"""
        super().__init__(data=data)

    @classmethod
    def from_label(cls, label):
        """todo"""
        data = cls._init_from_label(label)
        return cls(data=data)

    @classmethod
    def from_circuit(cls, circuit):
        """todo"""
        data = cls._init_from_circuit(circuit)
        return cls(data=data)

    @staticmethod
    def _init_from_label(label):
        """todo"""
        char2gate = {
            'I': IGate(), 'X': XGate(), 'Y': YGate(), 'Z': ZGate(),
            'H': HGate(), 'S': SGate(), 'T': TGate()
        }
        if re.match(r'^[IXYZHST]+$', label) is None:
            raise ValueError
        return TensorProduct(*[char2gate[char].to_sympy() for char in label])

    @staticmethod
    def _init_from_circuit(circuit):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from ..utils import flatten_circuit, transpile_circuit
        circuit = transpile_circuit(flatten_circuit(circuit))
        gph = exp(I * circuit.global_phase)
        circ_data = Operator._get_circ_data(circuit)
        return gph * math.prod(TensorProduct(*[gate.to_sympy() for gate in layer[::-1]
                                               if gate is not None]) for layer in circ_data[::-1])

    @staticmethod
    def _get_circ_data(circuit):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ..utils import get_layers_data
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
        return circ_data

    def to_numpy(self):
        """todo"""
        try:
            return matrix2numpy(self.to_sympy(), dtype=complex)
        except TypeError:
            return matrix2numpy(self.to_sympy(), dtype=object)

    def dot(self, other):
        """todo"""
        if not isinstance(other, Operator):
            other = Operator(other)
        dotprod = self.to_sympy() @ other.to_sympy()
        return self.__class__(dotprod)
