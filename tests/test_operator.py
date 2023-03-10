"""Test operator module"""

import numpy
from hypothesis import given, settings, strategies
from qiskit.quantum_info import Operator
from qiskit_symbolic.random import random_parametric_circuit
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


@given(num_qubits=strategies.integers(min_value=1, max_value=3),
       seed=strategies.integers(min_value=0, max_value=2**32-1))
@settings(max_examples=20, deadline=None)
def test_from_circuit(num_qubits, seed):
    """todo"""
    numpy.random.seed(seed)
    circuit, params = random_parametric_circuit(
        num_qubits=num_qubits, depth=3, seed=seed)
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    params_dict = dict(zip(params, values))
    qiskit_circ = circuit.assign_parameters(params_dict)
    arr1 = Operator(qiskit_circ).data
    symb_operator = symb_Operator(circuit)
    arr2 = symb_operator.subs(params_dict).to_numpy()
    assert numpy.allclose(arr1, arr2)
