"""Layer-wise symbolic simulator module."""

from dataclasses import dataclass
from functools import reduce
import numpy
from qiskit.circuit import ParameterVector
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.quantum_info import Statevector as QiskitStatevector
from .quantum_info import Operator


@dataclass
class CompiledCircuit:
    """todo"""

    num_qubits: int
    layer_funcs: list
    layer_args: list


class Simulator:
    """Layer-wise symbolic simulator for repeated circuit evaluations."""

    def __init__(self, backend="numpy"):
        """todo"""
        self._backend = backend

    @staticmethod
    def compile(circ):
        """todo"""
        operators = [
            Operator(dag_to_circuit(layer["graph"]))
            for layer in circuit_to_dag(circ).layers()
        ]
        return CompiledCircuit(
            num_qubits=circ.num_qubits,
            layer_funcs=[op.to_lambda() for op in operators],
            layer_args=[op._params for op in operators],
        )

    @staticmethod
    def _flat_params_dict(params_dict):
        """todo"""
        flat_params = {}
        for param, values in params_dict.items():
            if isinstance(param, ParameterVector):
                for p, values in zip(param, zip(*values)):
                    flat_params[p] = values
            else:
                flat_params[param] = values
        return flat_params

    @staticmethod
    def _run_once(compiled_circ, arg_values):
        """todo"""
        nq = compiled_circ.num_qubits
        zeros_state = QiskitStatevector.from_label("0" * nq).data
        unitaries = (
            func(*(arg_values[arg] for arg in args))
            for func, args in zip(compiled_circ.layer_funcs, compiled_circ.layer_args)
        )
        return reduce(lambda psi, u: numpy.matmul(u, psi), unitaries, zeros_state)

    def run(self, compiled_circ, params_dict):
        """todo"""
        flat_params = self._flat_params_dict(params_dict=params_dict)
        num_reps = len(next(iter(flat_params.values())))
        return [
            self._run_once(
                compiled_circ=compiled_circ,
                arg_values={arg: values[i] for arg, values in flat_params.items()},
            )
            for i in range(num_reps)
        ]
