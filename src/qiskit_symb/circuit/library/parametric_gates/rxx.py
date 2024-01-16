r"""Symbolic :math:`RXX(\theta)` and controlled-:math:`RXX(\theta)` gates module"""
import sympy
from sympy import Matrix
from sympy.physics.quantum import TensorProduct
from qiskit_symb import DensityMatrix
from ...gate import Gate
from ...controlledgate import ControlledGate


class RXXGate(Gate):
    r"""Symbolic :math:`RXX(\theta)` gate class"""

    def __init__(self, theta, qubits=None):
        """todo"""
        params = [theta]
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='rxx', num_qubits=2, params=params, qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ...library import IGate, RXGate
        theta, = self._get_params_expr()
        qubits = [qbit - min(self.qubits) for qbit in self.qubits]
        term0 = [IGate().__sympy__()] * self._size
        term0[qubits[0]] = RXGate(theta).__sympy__()
        term0[qubits[1]] = DensityMatrix.from_label('+')._data
        term1 = [IGate().__sympy__()] * self._size
        term1[qubits[0]] = RXGate(-theta).__sympy__()
        term1[qubits[1]] = DensityMatrix.from_label('-')._data
        return TensorProduct(*term0[::-1]) + TensorProduct(*term1[::-1])


class CRXXGate(ControlledGate):
    r"""Symbolic controlled-:math:`CRXX` gate class"""

    def __init__(self, theta, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        params = [theta]
        base_gate = RXXGate(theta, qubits=target_qubits)
        super().__init__(name='crxx', num_qubits=3, params=params,
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)


class XXMinusYYGate(Gate):
    r"""Symbolic :math:`XXMinusYYGate(\theta)` gate class"""

    def __init__(self, theta, beta=0, qubits=None):
        """todo"""
        params = [theta, beta]
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='xx_minus_yy', num_qubits=2, params=params, qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ...library import IGate, RXGate

        theta, beta = self._get_params_expr()
        cos = sympy.cos(theta/2)
        sin = sympy.sin(theta/2)
        i = sympy.I
        exp = sympy.exp
        return Matrix([
                [cos, 0, 0, -i * sin * exp(-i * beta)],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [-i * sin * exp(i * beta), 0, 0, cos],
            ])

class XXPlusYYGate(Gate):
    r"""Symbolic :math:`XXPlusYYGate(\theta)` gate class"""

    def __init__(self, theta, beta=0, qubits=None):
        """todo"""
        params = [theta, beta]
        qubits = [0, 1] if qubits is None else qubits
        super().__init__(name='xx_minus_yy', num_qubits=2, params=params, qubits=qubits)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ...library import IGate, RXGate
        """

        return numpy.array(
            [
                [1, 0, 0, 0],
                [0, cos, -1j * sin * exp(-1j * beta), 0],
                [0, -1j * sin * exp(1j * beta), cos, 0],
                [0, 0, 0, 1],
            ]
        """
        theta, beta = self._get_params_expr()
        cos = sympy.cos(theta/2)
        sin = sympy.sin(theta/2)
        i = sympy.I
        exp = sympy.exp
        return Matrix([
                [1, 0, 0, 0],
                [0, cos, -i * sin * exp(-i * beta), 0],
                [0, -i * sin * exp(i * beta), cos, 0],
                [0, 0, 0, 1],
            ])
