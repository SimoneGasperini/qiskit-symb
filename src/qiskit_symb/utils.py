"""Utilities module"""

import random
from sympy import Symbol, sympify
from .circuit.library import NAME_TO_INIT


def get_init(name):
    """todo"""
    if name not in NAME_TO_INIT:
        raise NotImplementedError(
            f'Instruction "{name}" is not implemented in qiskit-symb')
    return NAME_TO_INIT[name]


def get_symbolic_gates_names():
    """todo"""
    return set(NAME_TO_INIT.keys())


def get_symbolic_expr(par_expr):
    """todo"""
    if hasattr(par_expr, '_symbol_expr'):
        return sympify(par_expr._symbol_expr)
    return par_expr


def get_unique_symbols(par_expr):
    """todo"""
    if hasattr(par_expr, '_parameter_symbols'):
        return list(dict.fromkeys([sympify(symb) for symb in par_expr._parameter_symbols.values()]))
    return []


def symbols2real(sympy_expr):
    """todo"""
    args_dict = {symbol: Symbol(symbol.name, real=True)
                 for symbol in sympy_expr.free_symbols}
    return sympy_expr.subs(args_dict)


def get_random_params(params_dict, size, seed=None):
    """todo"""
    random.seed(seed)
    parnames = list(params_dict.keys())
    params = list(zip(*[[random.randint(*params_dict[parname]) for _ in range(size)]
                        for parname in parnames]))
    ids = [','.join([f'{parname}={parval}'
                     for parname, parval in zip(parnames, parvals)])
           for parvals in params]
    return params, ids
