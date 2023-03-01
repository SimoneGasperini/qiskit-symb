"""Utilities module"""

from sympy import Symbol
from .library import NAME_TO_INIT  # pylint: disable=cyclic-import


def get_init(name):
    """todo"""
    return NAME_TO_INIT[name]


def symbols2real(expression):
    """todo"""
    args_dict = {symbol: Symbol(symbol.name, real=True)
                 for symbol in expression.free_symbols}
    return expression.subs(args_dict)
