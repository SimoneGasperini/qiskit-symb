"""Symbolic matrix operator module"""

import re
import math
import numpy
import sympy
from sympy.matrices import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit import QuantumCircuit
from .gate import Gate
from .controlledgate import ControlledGate
from .library.standard_gates import IGate, XGate, YGate, ZGate, HGate, SGate, TGate


class Operator:
    """Symbolic matrix operator class"""

    def __init__(self, data):
        """todo"""
        # pylint: disable=duplicate-code
        if isinstance(data, Matrix):
            self._data = data
        elif isinstance(data, (list, numpy.ndarray)):
            self._data = Matrix(data)
        elif isinstance(data, QuantumCircuit):
            self._data = self._init_from_circuit(data)
        elif isinstance(data, type(self)):
            self._data = data._data
        else:
            raise TypeError

    @classmethod
    def from_label(cls, label):
        """todo"""
        char2matrix = {
            'I': IGate().to_sympy(),
            'X': XGate().to_sympy(),
            'Y': YGate().to_sympy(),
            'Z': ZGate().to_sympy(),
            'H': HGate().to_sympy(),
            'S': SGate().to_sympy(),
            'T': TGate().to_sympy()
        }
        if re.match(r'^[IXYZHST]+$', label) is None:
            raise ValueError
        one_qubit_ops = [char2matrix[char] for char in label]
        data = TensorProduct(*one_qubit_ops)
        return cls(data=data)

    @staticmethod
    def _init_from_circuit(circuit):
        """todo"""
        # pylint: disable=import-outside-toplevel
        from .utils import flatten_circuit, transpile_circuit
        circuit = transpile_circuit(flatten_circuit(circuit))
        gph = sympy.exp(sympy.I * circuit.global_phase)
        circ_data = Operator._get_circ_data(circuit)
        return gph * math.prod(TensorProduct(*[gate.to_sympy() for gate in layer[::-1]
                                               if gate is not None]) for layer in circ_data[::-1])

    @staticmethod
    def _get_circ_data(circuit):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from .utils import get_layers_data
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

    def to_sympy(self):
        """todo"""
        return self._data

    def to_numpy(self):
        """todo"""
        try:
            return numpy.array(self.to_sympy(), dtype=complex)
        except TypeError:
            return numpy.array(self.to_sympy(), dtype=object)

    def subs(self, params_dict):
        """todo"""
        sympy_matrix = self.to_sympy()
        name2symbol = {symbol.name: symbol
                       for symbol in sympy_matrix.free_symbols}
        symbol2value = {name2symbol[par.name]: value
                        for par, value in params_dict.items()}
        return self.__class__(sympy_matrix.subs(symbol2value))

    def transpose(self):
        """todo"""
        return self.__class__(self.to_sympy().transpose())

    def conjugate(self):
        """todo"""
        return self.__class__(self.to_sympy().conjugate())

    def dagger(self):
        """todo"""
        return self.__class__(self.to_sympy().transpose().conjugate())

    def dot(self, other):
        """todo"""
        if not isinstance(other, Operator):
            other = Operator(other)
        dotprod = self.to_sympy() @ other.to_sympy()
        return self.__class__(dotprod)
