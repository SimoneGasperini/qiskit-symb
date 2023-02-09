"""Symbolic gates library module"""

from .standard_gates import (
    IGate,
    XGate, CXGate,
    YGate,
    ZGate,
    HGate,
    SGate, SdgGate,
    TGate, TdgGate
)

from .parametric_gates import (
    UGate,
    RXGate,
    RYGate,
    RZGate,
    PhaseGate,
    RGate
)

NAME_TO_INIT = {
    'id': IGate,
    'x': XGate,
    'cx': CXGate,
    'y': YGate,
    'z': ZGate,
    'h': HGate,
    's': SGate,
    'sdg': SdgGate,
    't': TGate,
    'tdg': TdgGate,
    'u': UGate,
    'rx': RXGate,
    'ry': RYGate,
    'rz': RZGate,
    'p': PhaseGate,
    'r': RGate
}
