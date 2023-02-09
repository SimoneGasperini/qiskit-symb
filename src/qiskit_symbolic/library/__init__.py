"""Symbolic gates library module"""

from .standard_gates import (
    IGate,
    XGate, CXGate,
    YGate, CYGate,
    ZGate, CZGate,
    HGate, CHGate,
    SGate, SdgGate, CSGate, CSdgGate,
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
    'rx': RXGate,
    'ry': RYGate,
    'rz': RZGate,
    'p': PhaseGate,
    'r': RGate
}
