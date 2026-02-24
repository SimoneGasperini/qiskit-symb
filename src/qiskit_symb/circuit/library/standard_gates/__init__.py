"""Symbolic standard gates module"""

from .i import IGate
from .x import XGate, CXGate
from .y import YGate, CYGate
from .z import ZGate, CZGate
from .h import HGate, CHGate
from .sx import SXGate, SXdgGate, CSXGate, CSXdgGate
from .s import SGate, SdgGate, CSGate, CSdgGate
from .t import TGate, TdgGate, CTGate, CTdgGate
from .swap import SwapGate
from .iswap import iSwapGate
from .dcx import DCXGate
from .ecr import ECRGate

__all__ = [
    "IGate",
    "XGate",
    "CXGate",
    "YGate",
    "CYGate",
    "ZGate",
    "CZGate",
    "HGate",
    "CHGate",
    "SXGate",
    "SXdgGate",
    "CSXGate",
    "CSXdgGate",
    "SGate",
    "SdgGate",
    "CSGate",
    "CSdgGate",
    "TGate",
    "TdgGate",
    "CTGate",
    "CTdgGate",
    "SwapGate",
    "iSwapGate",
    "DCXGate",
    "ECRGate",
]
