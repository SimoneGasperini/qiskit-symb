"""Symbolic quantum circuit module"""

from qiskit.circuit.controlledgate import ControlledGate
from .library import *


name2class = {
    'id': IGate,
    'x': XGate,
    'cx': CXGate,
    'y': YGate,
    'cy': CYGate,
    'z': ZGate,
    'cz': CZGate,
    'h': HGate,
    'ch': CHGate,
    'sx': SXGate,
    'sxdg': SXdgGate,
    'csx': CSXGate,
    'csxdg': CSXdgGate,
    's': SGate,
    'sdg': SdgGate,
    'cs': CSGate,
    'csdg': CSdgGate,
    't': TGate,
    'tdg': TdgGate,
    'ct': CTGate,
    'ctdg': CTdgGate,
    'swap': SwapGate,
    'iswap': iSwapGate,
    'dcx': DCXGate,
    'ecr': ECRGate,
    'u': UGate,
    'cu': CUGate,
    'u1': U1Gate,
    'cu1': CU1Gate,
    'u2': U2Gate,
    'cu2': CU2Gate,
    'u3': U3Gate,
    'cu3': CU3Gate,
    'rx': RXGate,
    'crx': CRXGate,
    'ry': RYGate,
    'cry': CRYGate,
    'rz': RZGate,
    'crz': CRZGate,
    'p': PhaseGate,
    'cp': CPhaseGate,
    'r': RGate,
    'cr': CRGate,
    'rxx': RXXGate,
    'ryy': RYYGate,
    'rzz': RZZGate,
    'rzx': RZXGate,
    'xx_minus_yy': XXMinusYYGate,
    'xx_plus_yy': XXPlusYYGate,
}


def get_class(op):
    """todo"""
    if isinstance(op, ControlledGate):
        name = 'c' + op.base_gate.name
    else:
        name = op.name
    try:
        return name2class[name]
    except KeyError as kerr:
        error_message = f'Gate "{name}" is not implemented in qiskit-symb'
        raise NotImplementedError(error_message) from kerr
