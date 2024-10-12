import random


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
