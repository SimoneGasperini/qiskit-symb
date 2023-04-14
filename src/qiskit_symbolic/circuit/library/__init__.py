"""Symbolic gates library module"""

from .standard_gates import (
    IGate,
    XGate, CXGate,
    YGate, CYGate,
    ZGate, CZGate,
    HGate, CHGate,
    SGate, SdgGate, CSGate, CSdgGate,
    TGate, TdgGate,
    SwapGate,
    iSwapGate
)

from .parametric_gates import (
    UGate, CUGate,
    RXGate, CRXGate,
    RYGate, CRYGate,
    RZGate, CRZGate,
    PhaseGate, CPhaseGate,
    RGate
)

NAME_TO_INIT = {
    'id': IGate,
    'x': XGate,
    'cx': CXGate,
    'y': YGate,
    'cy': CYGate,
    'z': ZGate,
    'cz': CZGate,
    'h': HGate,
    'ch': CHGate,
    's': SGate,
    'sdg': SdgGate,
    'cs': CSGate,
    'csdg': CSdgGate,
    't': TGate,
    'tdg': TdgGate,
    'u': UGate,
    'cu': CUGate,
    'rx': RXGate,
    'crx': CRXGate,
    'ry': RYGate,
    'cry': CRYGate,
    'rz': RZGate,
    'crz': CRZGate,
    'p': PhaseGate,
    'cp': CPhaseGate,
    'r': RGate,
    'swap': SwapGate,
    'iswap': iSwapGate
}
