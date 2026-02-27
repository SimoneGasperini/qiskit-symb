"""Test symbolic simulator module."""

import numpy
import pytest
from hypothesis import given, settings, strategies
from qiskit.quantum_info import Statevector
from qiskit_symb import Simulator
from qiskit_symb.circuit.random import random_parametric_circuit


@pytest.mark.parametrize("splitting", ["layers", "barriers"])
@given(num_qubits=strategies.integers(min_value=1, max_value=5))
@settings(deadline=None)
def test_execution(num_qubits, splitting):
    """todo"""
    pqc1 = random_parametric_circuit(num_qubits, par_prefix="x", depth=2)
    pqc1.barrier()
    pqc2 = random_parametric_circuit(num_qubits, par_prefix="y", depth=3)
    pqc = pqc1.compose(pqc2)
    params = tuple(pqc.parameters)
    data = numpy.random.rand(5, len(params)) * 2 * numpy.pi
    simulator = Simulator(splitting=splitting)
    compiled_qc = simulator.compile(pqc)
    params_dict = dict(zip(params, data.transpose()))
    results = simulator.run(compiled_qc, params_dict=params_dict)
    for i in range(len(data)):
        qiskit_circ = pqc.assign_parameters(dict(zip(params, data[i])))
        arr1 = Statevector(qiskit_circ).data
        arr2 = results[i]
        assert numpy.allclose(arr1, arr2)
