"""Utilities module"""

from sympy import Symbol, sympify
from .library import NAME_TO_INIT  # pylint: disable=cyclic-import


def get_init(name):
    """todo"""
    return NAME_TO_INIT[name]


def get_symbolic_expr(par_expr):
    """todo"""
    # pylint: disable=protected-access
    if hasattr(par_expr, '_symbol_expr'):
        return sympify(par_expr._symbol_expr)
    return par_expr


def get_unique_symbols(par_expr):
    """todo"""
    # pylint: disable=protected-access
    if hasattr(par_expr, '_parameter_symbols'):
        return list(dict.fromkeys([sympify(symb) for symb in par_expr._parameter_symbols.values()]))
    return []


def symbols2real(sympy_expr):
    """todo"""
    args_dict = {symbol: Symbol(symbol.name, real=True)
                 for symbol in sympy_expr.free_symbols}
    return sympy_expr.subs(args_dict)
