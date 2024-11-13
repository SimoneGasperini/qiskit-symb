"""todo"""

from sympy import Matrix, I, pi, sin, cos, exp
from ...parametricgate import ParametricGate
from ...controlledgate import ControlledGate


class UGate(ParametricGate):
    r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate class"""
    gate_name = 'U'
    gate_name_latex = r'\text{U}'

    def __new__(cls, theta, phi, lam, target, _gamma=0):
        """todo"""
        params = (theta, phi, lam, _gamma)
        qubits = (target,)
        return super().__new__(cls, params=params, qubits=qubits)

    def __init__(self, theta, phi, lam, target, _gamma=0):
        """todo"""
        self.params = (theta, phi, lam, _gamma)
        self.qubits = (target,)

    def _sympy_matrix(self):
        """todo"""
        theta, phi, lam, gamma = self.get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        expphi = exp(I * phi)
        explam = exp(I * lam)
        expphilam = exp(I * (phi + lam))
        expgam = exp(I * gamma)
        return expgam * Matrix([[costh2, -explam*sinth2],
                                [expphi*sinth2, expphilam*costh2]])


class U1Gate(UGate):
    r"""Symbolic :math:`U1(\lambda)` gate class"""
    gate_name = 'U'
    gate_name_latex = r'\text{U}'

    def __new__(cls, lam, target):
        """todo"""
        theta = 0
        phi = 0
        return super().__new__(cls, theta=theta, phi=phi, lam=lam, target=target)

    def __init__(self, lam, target):
        """todo"""
        theta = 0
        phi = 0
        super().__init__(theta=theta, phi=phi, lam=lam, target=target)


class U2Gate(UGate):
    r"""Symbolic :math:`U2(\phi, \lambda)` gate class"""
    gate_name = 'U'
    gate_name_latex = r'\text{U}'

    def __new__(cls, phi, lam, target):
        """todo"""
        theta = pi / 2
        return super().__new__(cls, theta=theta, phi=phi, lam=lam, target=target)

    def __init__(self, phi, lam, target):
        """todo"""
        theta = pi / 2
        super().__init__(theta=theta, phi=phi, lam=lam, target=target)


class U3Gate(UGate):
    r"""Symbolic :math:`U3(\theta, \phi, \lambda)` gate class"""
    gate_name = 'U'
    gate_name_latex = r'\text{U}'

    def __new__(cls, theta, phi, lam, target):
        """todo"""
        return super().__new__(cls, theta=theta, phi=phi, lam=lam, target=target)

    def __init__(self, theta, phi, lam, target):
        """todo"""
        super().__init__(theta=theta, phi=phi, lam=lam, target=target)


class CUGate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gate class"""
    gate_name = 'CU'
    gate_name_latex = r'\text{CU}'

    def __new__(cls, theta, phi, lam, gamma, control, target):
        """todo"""
        controls = (control,)
        target_gate = UGate(theta=theta, phi=phi, lam=lam,
                            _gamma=gamma, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, theta, phi, lam, gamma, control, target):
        """todo"""
        target_gate = UGate(theta=theta, phi=phi, lam=lam,
                            _gamma=gamma, target=target)
        self.params = target_gate.params
        self.qubits = (control, target)


class CU1Gate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`U1(\lambda)` gate class"""
    gate_name = 'CU'
    gate_name_latex = r'\text{CU}'

    def __new__(cls, lam, control, target):
        """todo"""
        controls = (control,)
        target_gate = U1Gate(lam=lam, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, lam, control, target):
        """todo"""
        target_gate = U1Gate(lam=lam, target=target)
        self.params = target_gate.params
        self.qubits = (control, target)


class CU2Gate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`U2(\phi, \lambda)` gate class"""
    gate_name = 'CU'
    gate_name_latex = r'\text{CU}'

    def __new__(cls, phi, lam, control, target):
        """todo"""
        controls = (control,)
        target_gate = U2Gate(phi=phi, lam=lam, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, phi, lam, control, target):
        """todo"""
        target_gate = U2Gate(phi=phi, lam=lam, target=target)
        self.params = target_gate.params
        self.qubits = (control, target)


class CU3Gate(ControlledGate, ParametricGate):
    r"""Symbolic controlled-:math:`U3(\theta, \phi, \lambda)` gate class"""
    gate_name = 'CU'
    gate_name_latex = r'\text{CU}'

    def __new__(cls, theta, phi, lam, control, target):
        """todo"""
        controls = (control,)
        target_gate = U3Gate(theta=theta, phi=phi, lam=lam, target=target)
        return super().__new__(cls, controls=controls, target_gate=target_gate)

    def __init__(self, theta, phi, lam, control, target):
        """todo"""
        target_gate = U3Gate(theta=theta, phi=phi, lam=lam, target=target)
        self.params = target_gate.params
        self.qubits = (control, target)
