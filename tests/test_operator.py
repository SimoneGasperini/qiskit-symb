"""Test operator module"""

import numpy
from hypothesis import given, settings, strategies
from qiskit.circuit.random import random_circuit
from qiskit.quantum_info import Operator
from qiskit_symbolic.operator import Operator as symb_Operator


@given(seed=strategies.integers(min_value=0))
@settings(max_examples=10, deadline=None)
def test_operator_from_circuit(seed):
    """todo"""
    circuit = random_circuit(num_qubits=3, depth=4, seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)
