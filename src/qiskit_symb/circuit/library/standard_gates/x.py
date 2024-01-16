r"""Symbolic Pauli :math:`X` and controlled-:math:`X` gates module"""
import sympy
from sympy.matrices import Matrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class XGate(Gate):
    r"""Symbolic Pauli :math:`X` gate class"""

    def __init__(self):
        """todo"""
        super().__init__(name='x', num_qubits=1, params=[])

    def __sympy__(self):
        """todo"""
        return Matrix([[0, 1],
                       [1, 0]])


class CXGate(ControlledGate):
    r"""Symbolic controlled-:math:`X` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = XGate()
        super().__init__(name='cx', num_qubits=2, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)

class CCXGate(ControlledGate):
    r"""Symbolic controlled-:math:`CCX` gate class"""

    def __init__(self, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        base_gate = CXGate()
        super().__init__(name='ccx', num_qubits=3, params=[],
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)


class RCCXGate(Gate):
    r"""Symbolic controlled-:math:`RCCX` gate class"""

    def __init__(self, qubits=None):
        """todo"""
        qubits = [0, 1, 2] if qubits is None else qubits
        super().__init__(name='rccx', num_qubits=3, params=[], qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ...library import IGate, RXGate
        i = sympy.I
        return Matrix([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, -i],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, i, 0, 0, 0, 0],
        ])


class RC3XGate(Gate):
    r"""Symbolic controlled-:math:`RC3X` gate class"""

    def __init__(self, qubits=None):
        """todo"""
        qubits = [0, 1, 2, 3] if qubits is None else qubits
        super().__init__(name='rcccx', num_qubits=4, params=[], qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ...library import IGate, RXGate
        i = sympy.I
        return Matrix([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, i, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -i, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        ])


class DCXGate(Gate):
    r"""Symbolic controlled-:math:`DCX` gate class"""

    def __init__(self, qubits=None):
        """todo"""
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='dcx', num_qubits=2, params=[], qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ...library import IGate, RXGate
        return Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]])
