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
    'u': UGate,
    'u3': UGate,
    'cu': CUGate,
    'cu3': CUGate,
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
}


def get_class(op):
    """todo"""
    if isinstance(op, ControlledGate):
        name = 'c' + op.base_gate.name
    else:
        name = op.name
    try:
        return name2class[name]
    except KeyError:
        error_message = f'Gate "{name}" is not implemented in qiskit-symb'
        raise NotImplementedError(error_message)


basis_gates = set(name2class.keys())
