"""todo"""

from sympy import sin, cos, exp
from sympy.tensor.array import Array
from ...parametricgate import ParametricGate


class UGate(ParametricGate):
    r"""Symbolic :math:`U(\theta, \phi, \lambda)` gate class"""

    def __init__(self, theta, phi, lam, qubit, _gamma=0):
        """todo"""
        params = (theta, phi, lam, _gamma)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, phi, lam, gamma = self._get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        expphi = exp(1j * phi)
        explam = exp(1j * lam)
        expphilam = exp(1j * (phi + lam))
        expgam = exp(1j * gamma)
        return Array([[expgam*costh2, -expgam*explam*sinth2],
                      [expgam*expphi*sinth2, expgam*expphilam*costh2]])


class U1Gate(ParametricGate):
    r"""Symbolic :math:`U1(\lambda)` gate class"""

    def __init__(self, lam, qubit):
        """todo"""
        params = (lam,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        lam, = self._get_params_expr()
        explam = exp(1j * lam)
        return Array([[1, 0],
                      [0, explam]])


class U2Gate(ParametricGate):
    r"""Symbolic :math:`U2(\phi, \lambda)` gate class"""

    def __init__(self, phi, lam, qubit):
        """todo"""
        params = (phi, lam,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        phi, lam = self._get_params_expr()
        expphi = exp(1j * phi)
        explam = exp(1j * lam)
        expphilam = exp(1j * (phi + lam))
        x = 1 / 2**0.5
        return Array([[x, -x*explam],
                      [x*expphi, x*expphilam]])


class U3Gate(ParametricGate):
    r"""Symbolic :math:`U3(\theta, \phi, \lambda)` gate class"""

    def __init__(self, theta, phi, lam, qubit):
        """todo"""
        params = (theta, phi, lam,)
        qubits = (qubit,)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, phi, lam = self._get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        expphi = exp(1j * phi)
        explam = exp(1j * lam)
        expphilam = exp(1j * (phi + lam))
        return Array([[costh2, -explam*sinth2],
                      [expphi*sinth2, expphilam*costh2]])


class CUGate(ParametricGate):
    r"""Symbolic controlled-:math:`U(\theta, \phi, \lambda, \gamma)` gate class"""

    def __init__(self, theta, phi, lam, gamma, control, target):
        """todo"""
        params = (theta, phi, lam, gamma)
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, phi, lam, gamma = self._get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        expphi = exp(1j * phi)
        explam = exp(1j * lam)
        expphilam = exp(1j * (phi + lam))
        expgam = exp(1j * gamma)
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, expgam*costh2, -expgam*explam*sinth2],
                      [0, 0, expgam*expphi*sinth2, expgam*expphilam*costh2]])


class CU1Gate(ParametricGate):
    r"""Symbolic controlled-:math:`U1(\lambda)` gate class"""

    def __init__(self, lam, control, target):
        """todo"""
        params = (lam,)
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        lam, = self._get_params_expr()
        explam = exp(1j * lam)
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, explam]])


class CU2Gate(ParametricGate):
    r"""Symbolic controlled-:math:`U2(\phi, \lambda)` gate class"""

    def __init__(self, phi, lam, control, target):
        """todo"""
        params = (phi, lam)
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        phi, lam = self._get_params_expr()
        expphi = exp(1j * phi)
        explam = exp(1j * lam)
        expphilam = exp(1j * (phi + lam))
        x = 1 / 2**0.5
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, x, -x*explam],
                      [0, 0, x*expphi, x*expphilam]])


class CU3Gate(ParametricGate):
    r"""Symbolic controlled-:math:`U3(\theta, \phi, \lambda)` gate class"""

    def __init__(self, theta, phi, lam, control, target):
        """todo"""
        params = (theta, phi, lam)
        qubits = (control, target)
        super().__init__(params=params, qubits=qubits)

    def _sympy_array(self):
        """todo"""
        theta, phi, lam = self._get_params_expr()
        costh2 = cos(theta / 2)
        sinth2 = sin(theta / 2)
        expphi = exp(1j * phi)
        explam = exp(1j * lam)
        expphilam = exp(1j * (phi + lam))
        return Array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, costh2, -explam*sinth2],
                      [0, 0, expphi*sinth2, expphilam*costh2]])
