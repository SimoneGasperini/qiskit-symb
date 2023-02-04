"""Symbolic standard gates module"""

import sympy
from sympy.matrices import Matrix
from qiskit.circuit.library import UGate, RXGate, RYGate, RZGate
from qiskit_symbolic.gatesymb import GateSymb  # pylint: disable=cyclic-import


class UGateSymb(UGate, GateSymb):
    r"""Symbolic gate :math:`U(\theta, \phi, \lambda)` class"""

    def __init__(self, theta, phi, lam, qubits=None, label=None):
        """todo"""
        # pylint: disable=too-many-arguments
        super().__init__(theta=theta, phi=phi, lam=lam, label=label)
        self.qubits = qubits

    def __sympy__(self):
        """todo"""
        theta, phi, lam = self.get_sympy_params()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        exp = sympy.exp
        return Matrix([[cos, -exp(i * lam) * sin],
                       [exp(i * phi) * sin, exp(i * (phi + lam)) * cos]])


class RXGateSymb(RXGate, GateSymb):
    r"""Symbolic gate :math:`RX(\theta)` class"""

    def __init__(self, theta, qubits=None, label=None):
        """todo"""
        super().__init__(theta=theta, label=label)
        self.qubits = qubits

    def __sympy__(self):
        """todo"""
        theta, = self.get_sympy_params()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        return Matrix([[cos, -i * sin],
                       [-i * sin, cos]])


class RYGateSymb(RYGate, GateSymb):
    r"""Symbolic gate :math:`RY(\theta)` class"""

    def __init__(self, theta, qubits=None, label=None):
        """todo"""
        super().__init__(theta=theta, label=label)
        self.qubits = qubits

    def __sympy__(self):
        """todo"""
        theta, = self.get_sympy_params()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        return Matrix([[cos, -sin],
                       [sin, cos]])


class RZGateSymb(RZGate, GateSymb):
    r"""Symbolic gate :math:`RZ(\lambda)` class"""

    def __init__(self, phi, qubits=None, label=None):
        """todo"""
        super().__init__(phi=phi, label=label)
        self.qubits = qubits

    def __sympy__(self):
        """todo"""
        lam, = self.get_sympy_params()
        i = sympy.I
        return Matrix([[sympy.exp(-i * lam/2), 0],
                       [0, sympy.exp(i * lam/2)]])
