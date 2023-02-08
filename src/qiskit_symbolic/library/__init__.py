"""Symbolic gates library module"""

from .standard_gates import (
    IGate,
    XGate,
    CXGate,
    YGate,
    ZGate,
    HGate
)

from .parametric_gates import (
    UGate,
    RXGate,
    RYGate,
    RZGate
)

NAME_TO_INIT = {
    'id': IGate,
    'x': XGate,
    'cx': CXGate,
    'y': YGate,
    'z': ZGate,
    'h': HGate,
    'u': UGate,
    'rx': RXGate,
    'ry': RYGate,
    'rz': RZGate
}
