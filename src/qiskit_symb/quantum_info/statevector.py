"""Symbolic quantum statevector module."""

from .base import SymbQuantumObject
from .mpo import MPOFramework


class Statevector(SymbQuantumObject):
    """Symbolic quantum statevector class."""

    @staticmethod
    def _get_sympy_expr(circuit):
        """todo"""
        return MPOFramework.build_statevector(circuit)
