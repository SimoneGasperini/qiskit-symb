r"""Symbolic :math:`RXX(\theta)` and controlled-:math:`RXX(\theta)` gates module"""

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
    r"""Symbolic controlled-:math:`RXX` gate class"""

    def __init__(self, theta, ctrl_qubits=None, target_qubits=None, ctrl_state=None):
        """todo"""
        params = [theta]
        base_gate = RXXGate(theta, qubits=target_qubits)
        super().__init__(name='crxx', num_qubits=3, params=params,
                         ctrl_qubits=ctrl_qubits, target_qubits=target_qubits,
                         ctrl_state=ctrl_state, base_gate=base_gate)
