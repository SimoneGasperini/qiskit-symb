"""Symbolic gates library module"""

from .standard_gates import (
    IGate,
    XGate, CXGate,
    YGate, CYGate,
    ZGate, CZGate,
    HGate, CHGate,
    SXGate, SXdgGate, CSXGate, CSXdgGate,
    SGate, SdgGate, CSGate, CSdgGate,
    TGate, TdgGate, CTGate, CTdgGate,
    SwapGate, CSwapGate,
    iSwapGate, CiSwapGate,
    ECRGate, CECRGate
)

from .parametric_gates import (
    UGate, CUGate,
    RXGate, CRXGate,
    RYGate, CRYGate,
    RZGate, CRZGate,
    PhaseGate, CPhaseGate,
    RGate, CRGate
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
    'swap': SwapGate,
    'cswap': CSwapGate,
    'iswap': iSwapGate,
    'ciswap': CiSwapGate,
    'ecr': ECRGate,
    'cecr': CECRGate
}
