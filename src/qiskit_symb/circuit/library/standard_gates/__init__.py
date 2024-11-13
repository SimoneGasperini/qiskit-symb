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
