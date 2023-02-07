"""Utilities module"""

import re
from qiskit.circuit import ParameterExpression
from .library import NAME_TO_INIT  # pylint: disable=cyclic-import


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
