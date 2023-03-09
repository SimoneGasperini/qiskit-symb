"""Test operator module"""

import numpy
from hypothesis import given, settings, strategies
from qiskit.circuit.random import random_circuit
from qiskit.quantum_info import Operator, random_unitary
from qiskit_symbolic.operator import Operator as symb_Operator


@given(num_qubits=strategies.integers(min_value=1, max_value=7),
       seed=strategies.integers(min_value=0, max_value=2**32-1))
@settings(deadline=None)
def test_from_label(num_qubits, seed):
    """todo"""
    numpy.random.seed(seed)
    chars = ['I', 'X', 'Y', 'Z', 'H', 'S', 'T']
    label = ''.join(numpy.random.choice(chars, size=num_qubits).tolist())
    arr1 = Operator.from_label(label).data
    arr2 = symb_Operator.from_label(label).to_numpy()
    assert numpy.allclose(arr1, arr2)


@given(seed=strategies.integers(min_value=0, max_value=2**32-1))
@settings(max_examples=10, deadline=None)
def test_from_circuit(seed):
    """todo"""
    circuit = random_circuit(num_qubits=3, depth=3, seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@given(num_qubits=strategies.integers(min_value=1, max_value=7),
       seed=strategies.integers(min_value=0, max_value=2**32-1))
@settings(max_examples=10, deadline=None)
def test_is_unitary(num_qubits, seed):
    """todo"""
    unitary_matrix = random_unitary(dims=2**num_qubits, seed=seed).data
    symb_operator = symb_Operator(unitary_matrix)
    assert symb_operator.is_unitary()
