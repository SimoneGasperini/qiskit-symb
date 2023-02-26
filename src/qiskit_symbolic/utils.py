"""Utilities module"""

from .library import NAME_TO_INIT  # pylint: disable=cyclic-import


def get_init(name):
    """todo"""
    return NAME_TO_INIT[name]
