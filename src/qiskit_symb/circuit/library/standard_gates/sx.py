r"""Symbolic :math:`\sqrt{X}`, :math:`\sqrt{X}^{\dagger}`, controlled-:math:`\sqrt{X}`,
and controlled-:math:`\sqrt{X}^{\dagger}` gates module"""

from sympy.tensor.array import Array
from ...standardgate import StandardGate


class SXGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[0.5+0.5j, 0.5-0.5j],
                      [0.5-0.5j, 0.5+0.5j]])


class SXdgGate(StandardGate):
    r"""Symbolic :math:`\sqrt{X}^{\dagger}` gate class"""

    def __init__(self, qubit):
        """todo"""
        params = ()
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    @staticmethod
    def _sympy_array():
        """todo"""
        return Array([[0.5-0.5j, 0.5+0.5j],
                      [0.5+0.5j, 0.5-0.5j]])


class CSXGate(StandardGate):
    r"""Symbolic controlled-:math:`\sqrt{X}` gate class"""

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
                      [0, 0, 0.5+0.5j, 0.5-0.5j],
                      [0, 0, 0.5-0.5j, 0.5+0.5j]])


class CSXdgGate(StandardGate):
    r"""Symbolic controlled-:math:`\sqrt{X}^{\dagger}` gate class"""

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
                      [0, 0, 0.5-0.5j, 0.5+0.5j],
                      [0, 0, 0.5+0.5j, 0.5-0.5j]])
