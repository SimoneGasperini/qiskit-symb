"""Symbolic quantum operator module."""

from .base import SymbQuantumObject
from .mpo import MPOFramework


class Operator(SymbQuantumObject):
    """Symbolic quantum operator class."""

    @staticmethod
    def _get_sympy_expr(circuit):
        """todo"""
        return MPOFramework.build_operator(circuit)
