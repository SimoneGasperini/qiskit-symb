import sympy
from sympy.matrices import Matrix
from qiskit.circuit.library import *
from qiskit_symbolic.gatesymb import GateSymb


class UGateSymb(UGate, GateSymb):

    def __init__(self, theta, phi, lam, qubits=None, label=None):
        super().__init__(theta=theta, phi=phi, lam=lam, label=label)
        self.qubits = qubits

    def __sympy__(self):
        theta, phi, lam = self.get_sympy_params()
        cos = sympy.cos(theta / 2)
        sin = sympy.sin(theta / 2)
        i = sympy.I
        exp = sympy.exp
        return Matrix([[cos, -exp(i * lam) * sin],
                       [exp(i * phi) * sin, exp(i * (phi + lam)) * cos]])


class RXGateSymb(RXGate, GateSymb):

    def __init__(self, theta, qubits=None, label=None):
        super().__init__(theta=theta, label=label)
        self.qubits = qubits

    def __sympy__(self):
        params = self.get_sympy_params()
        cos = sympy.cos(params[0] / 2)
        sin = sympy.sin(params[0] / 2)
        i = sympy.I
        return Matrix([[cos, -i * sin],
                       [-i * sin, cos]])
