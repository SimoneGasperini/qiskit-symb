r"""Symbolic :math:`S`, :math:`S^{\dagger}`, controlled-:math:`S`,
and controlled-:math:`S^{\dagger}` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class SGate(StandardGate):
    r"""Symbolic :math:`S` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, 1j]])


class SdgGate(StandardGate):
    r"""Symbolic :math:`S^{\dagger}` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, -1j]])


class CSGate(StandardGate):
    r"""Symbolic controlled-:math:`S` gate class"""

    def __init__(self, control, target):
        """todo"""
        params = ()
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1j]])


class CSdgGate(StandardGate):
    r"""Symbolic controlled-:math:`S^{\dagger}` gate class"""

    def __init__(self, control, target):
        """todo"""
        params = ()
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, -1j]])
