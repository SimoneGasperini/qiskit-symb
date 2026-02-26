"""Shared symbolic quantum object base class."""

import numpy
import sympy
from qiskit import QuantumCircuit


class SymbolicQuantumObject:
    """Common API for symbolic quantum objects."""

    def __init__(self, data, nqubits=None, params=None):
        """todo"""
        if isinstance(data, QuantumCircuit):
            nqubits = data.num_qubits
            params = tuple(data.parameters)
            data = self._get_sympy_expr(circuit=data)
        self._sympy_expr = data
        self._nqubits = nqubits
        self._params = params

    @staticmethod
    def _get_sympy_expr(circuit):
        """todo"""
        raise NotImplementedError

    @classmethod
    def from_circuit(cls, circuit):
        """todo"""
        sympy_expr = cls._get_sympy_expr(circuit=circuit)
        nqubits = circuit.num_qubits
        params = tuple(circuit.parameters)
        return cls(data=sympy_expr, nqubits=nqubits, params=params)

    @classmethod
    def from_sympy_expr(cls, sympy_expr, nqubits, params):
        """todo"""
        return cls(data=sympy_expr, nqubits=nqubits, params=params)

    def to_sympy(self, simplify=False):
        """todo"""
        return sympy.simplify(self._sympy_expr) if simplify else self._sympy_expr

    def to_numpy(self):
        """todo"""
        return numpy.array(self.to_sympy().tolist(), dtype=complex)

    def _lambdify(self, sympy_expr):
        """todo"""
        name2symb = {symb.name: symb for symb in sympy_expr.free_symbols}
        args = [
            name2symb[par.name] if par.name in name2symb else sympy.Symbol("_")
            for par in self._params
        ]
        return sympy.lambdify(
            args=args, expr=sympy_expr, modules="numpy", dummify=True, cse=True
        )

    def to_lambda(self):
        """todo"""
        sympy_expr = self.to_sympy()
        return self._lambdify(sympy_expr=sympy_expr)

    def subs(self, params_dict):
        """todo"""
        par2val = {}
        for par, val in params_dict.items():
            if hasattr(par, "__len__"):
                par2val.update(dict(zip(par, val)))
            else:
                par2val[par] = val
        sympy_expr = self.to_sympy()
        name2symb = {symb.name: symb for symb in sympy_expr.free_symbols}
        symb2val = {
            name2symb[par.name]: val
            for par, val in par2val.items()
            if par.name in name2symb
        }
        params = [par for par in self._params if par not in par2val]
        return self.from_sympy_expr(
            sympy_expr.subs(symb2val), nqubits=self._nqubits, params=params
        )
