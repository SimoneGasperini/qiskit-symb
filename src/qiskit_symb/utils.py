"""Utilities module"""

import random
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
