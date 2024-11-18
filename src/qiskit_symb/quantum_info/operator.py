"""Symbolic quantum operator module"""

from sympy.physics.quantum import represent
from .quantumbase import QuantumBase


class Operator(QuantumBase):
    """Symbolic quantum operator class"""

    @staticmethod
    def _get_sympy_expr(circuit):
        """todo"""
        unitary = QuantumBase._get_unitary(circuit=circuit)
        return represent(unitary, nqubits=circuit.num_qubits)
