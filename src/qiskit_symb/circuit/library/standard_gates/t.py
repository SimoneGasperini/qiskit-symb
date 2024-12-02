r"""Symbolic :math:`T`, :math:`T^{\dagger}`, controlled-:math:`T`,
and controlled-:math:`T^{\dagger}` gates module"""

from numpy import pi
from sympy import exp
from sympy.tensor.array import Array
from ...standardgate import StandardGate


class TGate(StandardGate):
    r"""Symbolic :math:`T` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, exp(1j*pi/4)]])


class TdgGate(StandardGate):
    r"""Symbolic :math:`T^{\dagger}` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[1, 0],
                      [0, exp(-1j*pi/4)]])


class CTGate(StandardGate):
    r"""Symbolic controlled-:math:`T` gate class"""

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
                      [0, 0, 0, exp(1j*pi/4)]])


class CTdgGate(StandardGate):
    r"""Symbolic controlled-:math:`T^{\dagger}` gate class"""

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
                      [0, 0, 0, exp(-1j*pi/4)]])
