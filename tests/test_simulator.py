"""Test symbolic simulator module."""

import numpy
from hypothesis import given, settings, strategies
from qiskit.quantum_info import Statevector
from qiskit_symb import Simulator
from qiskit_symb.circuit.random import random_parametric_circuit


@given(num_qubits=strategies.integers(min_value=1, max_value=6))
@settings(deadline=None)
def test_execution(num_qubits):
    """todo"""
    pqc = random_parametric_circuit(num_qubits, depth=4)
    params = tuple(pqc.parameters)
    data = numpy.random.rand(5, len(params)) * 2 * numpy.pi
    simulator = Simulator()
    compiled_qc = simulator.compile(pqc)
    params_dict = dict(zip(params, data.transpose()))
    results = simulator.run(compiled_qc, params_dict=params_dict)
    for i in range(len(data)):
        qiskit_circ = pqc.assign_parameters(dict(zip(params, data[i])))
        arr1 = Statevector(qiskit_circ).data
        arr2 = results[i]
        assert numpy.allclose(arr1, arr2)
