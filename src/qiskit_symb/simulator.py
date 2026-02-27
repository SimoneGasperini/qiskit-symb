"""Layer-wise symbolic simulator module."""

from dataclasses import dataclass
from functools import reduce
import numpy
from qiskit.circuit import QuantumCircuit, ParameterVector
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.quantum_info import Statevector as QiskitStatevector
from .quantum_info import Operator


def _split_by_barriers(circ):
    """todo"""
    nq, nc = circ.num_qubits, circ.num_clbits
    circ_list = [QuantumCircuit(nq, nc)]
    for ci in circ:
        sub_circ = circ_list[-1]
        op = ci.operation
        qubits = [sub_circ.qubits[circ.find_bit(q).index] for q in ci.qubits]
        clbits = [sub_circ.clbits[circ.find_bit(c).index] for c in ci.clbits]
        if op.name == "barrier":
            circ_list.append(QuantumCircuit(nq, nc))
        else:
            sub_circ.append(op, qargs=qubits, cargs=clbits)
    # global phase?
    return circ_list


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


@dataclass
class CompiledCircuit:
    """todo"""

    num_qubits: int
    layer_funcs: list
    layer_args: list


class Simulator:
    """Layer-wise symbolic simulator for repeated circuit evaluations."""

    def __init__(self, backend="numpy", splitting=None):
        """todo"""
        self._backend = backend
        self._splitting = splitting
        if splitting is not None:
            if splitting not in ["layers", "barriers"]:
                raise ValueError(
                    f"`splitting={splitting}` is not valid. Use 'layers' or 'barriers'."
                )

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

    def compile(self, circ):
        """todo"""
        if self._splitting == "layers":
            layers = circuit_to_dag(circ).layers()
            operators = [Operator(dag_to_circuit(lay["graph"])) for lay in layers]
        elif self._splitting == "barriers":
            circuits = _split_by_barriers(circ)
            operators = [Operator(qc) for qc in circuits]
        else:
            operators = [Operator(circ)]
        return CompiledCircuit(
            num_qubits=circ.num_qubits,
            layer_funcs=[op.to_lambda() for op in operators],
            layer_args=[op._params for op in operators],
        )

    def run(self, compiled_circ, params_dict):
        """todo"""
        flat_params = _flat_params_dict(params_dict=params_dict)
        num_reps = len(next(iter(flat_params.values())))
        return [
            self._run_once(
                compiled_circ=compiled_circ,
                arg_values={arg: values[i] for arg, values in flat_params.items()},
            )
            for i in range(num_reps)
        ]
