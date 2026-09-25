"""Symbolic standard gates module"""

from .dcx import DCXGate
from .ecr import ECRGate
from .h import CHGate, HGate
from .i import IGate
from .iswap import iSwapGate
from .s import CSdgGate, CSGate, SdgGate, SGate
from .swap import SwapGate
from .sx import CSXdgGate, CSXGate, SXdgGate, SXGate
from .t import CTdgGate, CTGate, TdgGate, TGate
from .x import CXGate, XGate
from .y import CYGate, YGate
from .z import CZGate, ZGate

__all__ = [
    "CHGate",
    "CSGate",
    "CSXGate",
    "CSXdgGate",
    "CSdgGate",
    "CTGate",
    "CTdgGate",
    "CXGate",
    "CYGate",
    "CZGate",
    "DCXGate",
    "ECRGate",
    "HGate",
    "IGate",
    "SGate",
    "SXGate",
    "SXdgGate",
    "SdgGate",
    "SwapGate",
    "TGate",
    "TdgGate",
    "XGate",
    "YGate",
    "ZGate",
    "iSwapGate",
]
