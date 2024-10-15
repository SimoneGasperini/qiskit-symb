"""Symbolic quantum density matrix module"""

from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum import Dagger, qapply
from .quantumbase import QuantumBase


class DensityMatrix(QuantumBase):
    """Symbolic quantum density matrix class"""

    @staticmethod
    def _get_data(circuit):
        """todo"""
        unitary = QuantumBase._get_unitary(circuit=circuit)
        ket = Qubit('0' * circuit.num_qubits)
        psi = qapply(unitary * ket)
        rho = qapply(psi * Dagger(psi))
        return rho
