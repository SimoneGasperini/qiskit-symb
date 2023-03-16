"""Test statevector module"""

import numpy
from hypothesis import given, settings, strategies
from qiskit.quantum_info import Statevector
from qiskit_symbolic.circuit.random import random_parametric_circuit
from qiskit_symbolic.quantum_info import Statevector as symb_Statevector


@given(num_qubits=strategies.integers(min_value=1, max_value=3),
       seed=strategies.integers(min_value=0, max_value=2**32-1))
@settings(max_examples=10, deadline=None)
def test_from_circuit(num_qubits, seed):
    """todo"""
    # pylint: disable=duplicate-code
    numpy.random.seed(seed)
    circuit, params = random_parametric_circuit(
        num_qubits=num_qubits, depth=4, seed=seed)
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    params_dict = dict(zip(params, values))
    qiskit_circ = circuit.assign_parameters(params_dict)
    arr1 = Statevector(qiskit_circ).data
    symb_psi = symb_Statevector(circuit)
    arr2 = symb_psi.subs(params_dict).to_numpy()
    assert numpy.allclose(arr1, arr2)
