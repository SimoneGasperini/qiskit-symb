"""Symbolic quantum operator module"""

from .quantumbase import QuantumBase


class Operator(QuantumBase):
    """Symbolic quantum operator class"""

    @staticmethod
    def _get_data(circuit):
        """todo"""
        unitary = QuantumBase._get_unitary(circuit=circuit)
        return unitary
