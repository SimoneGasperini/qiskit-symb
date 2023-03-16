"""Symbolic quantum operator module"""

import re
import math
from sympy import matrix2numpy, exp, I
from sympy.physics.quantum import TensorProduct
from .quantumbase import QuantumBase
from ..circuit.library import (
    IGate, XGate, YGate, ZGate,
    HGate, SGate, TGate
)


class Operator(QuantumBase):
    """Symbolic quantum operator class"""

    def __init__(self, data):
        """todo"""
        super().__init__(data=data)

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
        circ_data = QuantumBase._get_circ_data(circuit)
        return gph * math.prod(TensorProduct(*[gate.to_sympy() for gate in layer[::-1]
                                               if gate is not None]) for layer in circ_data[::-1])

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
