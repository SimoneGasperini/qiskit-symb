"""Symbolic quantum base module"""

from sympy import lambdify, Symbol
from sympy.matrices import matrix2numpy


class QuantumBase:
    """Abstract symbolic quantum base class"""

    def __init__(self, data, params):
        """todo"""
        self._data = data
        self._params = params

    @classmethod
    def from_label(cls, label):
        """todo"""
        # pylint: disable=no-member
        data = cls._get_data_from_label(label)
        return cls(data=data, params=[])

    @classmethod
    def from_circuit(cls, circuit):
        """todo"""
        # pylint: disable=no-member
        data = cls._get_data_from_circuit(circuit)
        params = list(circuit.parameters)
        return cls(data=data, params=params)

    def to_sympy(self):
        """todo"""
        return self._data

    def to_numpy(self):
        """todo"""
        try:
            return matrix2numpy(self.to_sympy(), dtype=complex)
        except TypeError:
            return matrix2numpy(self.to_sympy(), dtype=object)

    def to_lambda(self):
        """todo"""
        sympy_matrix = self.to_sympy()
        name2symb = {symb.name: symb for symb in sympy_matrix.free_symbols}
        symbs = [name2symb[par.name] if par.name in name2symb else Symbol('@')
                 for par in self._params]
        args = [Symbol(f'_arg{i}') for i in range(len(self._params))]
        expr = sympy_matrix.subs(dict(zip(symbs, args)))
        return lambdify(args=args, expr=expr, modules='numpy')

    def subs(self, params_dict):
        """todo"""
        par2val = {}
        for par, val in params_dict.items():
            if hasattr(par, '__len__'):
                par2val.update(dict(zip(par, val)))
            else:
                par2val[par] = val
        sympy_matrix = self.to_sympy()
        name2symb = {symb.name: symb for symb in sympy_matrix.free_symbols}
        symb2val = {name2symb[par.name]: val for par, val in par2val.items()
                    if par.name in name2symb}
        data = sympy_matrix.subs(symb2val)
        params = [par for par in self._params if par not in par2val]
        return self.__class__(data=data, params=params)

    def transpose(self):
        """todo"""
        return self.__class__(data=self.to_sympy().T,
                              params=self._params)

    def conjugate(self):
        """todo"""
        return self.__class__(data=self.to_sympy().conjugate(),
                              params=self._params)

    def dagger(self):
        """todo"""
        return self.__class__(data=self.to_sympy().T.conjugate(),
                              params=self._params)
