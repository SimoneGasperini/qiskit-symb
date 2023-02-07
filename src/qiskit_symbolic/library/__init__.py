"""Symbolic gates library module"""

from .standard_gates import (
    IGateSymb,
    XGateSymb,
    CXGateSymb,
    YGateSymb,
    ZGateSymb,
    HGateSymb
)

from .parametric_gates import (
    UGateSymb,
    RXGateSymb,
    RYGateSymb,
    RZGateSymb
)

NAME_TO_INIT = {
    'id': IGateSymb,
    'x': XGateSymb,
    'cx': CXGateSymb,
    'y': YGateSymb,
    'z': ZGateSymb,
    'h': HGateSymb,
    'u': UGateSymb,
    'rx': RXGateSymb,
    'ry': RYGateSymb,
    'rz': RZGateSymb
}
