"""Symbolic gates library module"""

from qiskit_symbolic.library.standard_gates import *


NAME_TO_INIT = {
    'u': UGateSymb,
    'rx': RXGateSymb,
    'ry': RYGateSymb,
    'rz': RZGateSymb
}
