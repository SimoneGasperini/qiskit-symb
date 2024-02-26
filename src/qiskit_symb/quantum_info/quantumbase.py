"""Symbolic quantum base module"""

import numpy
import sympy
from sympy import Symbol, lambdify
from sympy.matrices import Matrix, matrix2numpy
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider.basic_provider_tools import einsum_matmul_index


class QuantumBase:
    """Abstract symbolic quantum base class"""

    def __init__(self, data, params):
        """todo"""
        # pylint: disable=no-member
        if isinstance(data, QuantumCircuit):
            params = list(data.parameters)
            data = self._get_data_from_circuit(circuit=data)
        self._data = data
        self._params = params

    @staticmethod
    def _get_circ_unitary(circ):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from ..utils import transpile_circuit, flatten_circuit
        from ..circuit import Gate
        circ = transpile_circuit(flatten_circuit(circ))
        layers = circ.draw(output='text').nodes
        dim = 2 ** circ.num_qubits
        newshape = (2, 2) * circ.num_qubits
        unitary = numpy.reshape(numpy.eye(dim), newshape=newshape)
        for layer in layers:
            for instruction in layer[::-1]:
                gate_tensor = Gate.get(instruction)._get_tensor()
                gate_indices = [qarg._index for qarg in instruction.qargs]
                indexing = einsum_matmul_index(
                    gate_indices=gate_indices, number_of_qubits=circ.num_qubits)
                unitary = numpy.einsum(indexing, gate_tensor, unitary,
                                       dtype=object, casting='no', optimize='optimal')
        gph = sympy.exp(sympy.I * circ.global_phase)
        return gph * Matrix(numpy.reshape(unitary, newshape=(dim, dim)))

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
        return matrix2numpy(self._data, dtype=complex)

    def to_lambda(self):
        """todo"""
        sympy_matrix = self._data
        name2symb = {symb.name: symb for symb in sympy_matrix.free_symbols}
        args = [name2symb[par.name] if par.name in name2symb else Symbol('_')
                for par in self._params]
        return lambdify(args=args, expr=sympy_matrix, modules='numpy', dummify=True, cse=True)

    def subs(self, params_dict):
        """todo"""
        par2val = {}
        for par, val in params_dict.items():
            if hasattr(par, '__len__'):
                par2val.update(dict(zip(par, val)))
            else:
                par2val[par] = val
        sympy_matrix = self._data
        name2symb = {symb.name: symb for symb in sympy_matrix.free_symbols}
        symb2val = {name2symb[par.name]: val for par, val in par2val.items()
                    if par.name in name2symb}
        data = sympy_matrix.subs(symb2val)
        params = [par for par in self._params if par not in par2val]
        return self.__class__(data=data, params=params)

    def transpose(self):
        """todo"""
        return self.__class__(data=self._data.T, params=self._params)

    def conjugate(self):
        """todo"""
        return self.__class__(data=self._data.conjugate(), params=self._params)

    def dagger(self):
        """todo"""
        return self.__class__(data=self._data.T.conjugate(), params=self._params)
