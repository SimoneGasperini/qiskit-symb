"""Symbolic quantum statevector module"""

from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum import represent
from .quantumbase import QuantumBase


class Statevector(QuantumBase):
    """Symbolic quantum statevector class"""

    @staticmethod
    def _get_sympy_expr(circuit):
        """todo"""
        unitary = QuantumBase._get_unitary(circuit=circuit)
        ket = Qubit('0' * circuit.num_qubits)
        return represent(unitary * ket, nqubits=circuit.num_qubits)
