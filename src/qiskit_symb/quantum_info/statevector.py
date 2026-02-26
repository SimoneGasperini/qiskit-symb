"""Symbolic quantum statevector module."""

from .base import SymbolicQuantumObject
from .mpo import MPOFramework


class Statevector(SymbolicQuantumObject):
    """Symbolic quantum statevector class."""

    @staticmethod
    def _get_sympy_expr(circuit):
        """todo"""
        return MPOFramework.build_statevector(circuit)
