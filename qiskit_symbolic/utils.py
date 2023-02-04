"""Utilities module"""

import re
from qiskit.circuit.parameterexpression import ParameterExpression
from qiskit_symbolic.library import NAME_TO_INIT


def get_init(name):
    """todo"""
    return NAME_TO_INIT[name]


def sympify(par, chars_to_strip='][$'):
    """todo"""
    if not isinstance(par, ParameterExpression):
        return par
    state = par.__getstate__()
    state['name'] = re.sub(f'[{chars_to_strip}]', '', state['name'])
    par.__setstate__(state)
    return par.sympify()
