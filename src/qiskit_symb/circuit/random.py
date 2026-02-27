"""Random parametric circuit module"""

from qiskit.circuit import QuantumCircuit, ParameterVector
from qiskit.circuit.random import random_circuit


def random_parametric_circuit(
    num_qubits, depth, max_operands=3, par_prefix="x", seed=None
):
    """todo"""
    random_qc = random_circuit(
        num_qubits=num_qubits, depth=depth, max_operands=max_operands, seed=seed
    )
    random_pqc = QuantumCircuit(random_qc.num_qubits)
    num_params = sum(len(instruction.operation.params) for instruction in random_qc)
    par = ParameterVector(name=par_prefix, length=num_params)
    i = 0
    for instruction in random_qc:
        op = instruction.operation.to_mutable()
        n = len(op.params)
        op.params = par[i : i + n]
        i += n
        random_pqc.append(op, qargs=instruction.qubits)
    return random_pqc
