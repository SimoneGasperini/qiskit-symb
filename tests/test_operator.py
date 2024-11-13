"""Test operator module"""

import numpy
from hypothesis import given, strategies, settings
from qiskit.quantum_info import Operator
from qiskit_symb.quantum_info import Operator as symb_Operator
from qiskit_symb.circuit.random import random_parametric_circuit


@given(num_qubits=strategies.integers(min_value=1, max_value=3),
       seed=strategies.integers(min_value=0))
@settings(deadline=None)
def test_from_circuit(num_qubits, seed):
    """todo"""
    pqc = random_parametric_circuit(
        num_qubits=num_qubits, depth=4, seed=seed)
    params = pqc.parameters
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    par2val = dict(zip(params, values))
    qiskit_circ = pqc.assign_parameters(par2val)
    arr1 = Operator(qiskit_circ).data
    symb_op = symb_Operator.from_circuit(pqc)
    arr2 = symb_op.subs(par2val).to_numpy()
    assert numpy.allclose(arr1, arr2)


@given(num_qubits=strategies.integers(min_value=1, max_value=3),
       seed=strategies.integers(min_value=0))
@settings(deadline=None)
def test_to_lambda(num_qubits, seed):
    """todo"""
    pqc = random_parametric_circuit(
        num_qubits=num_qubits, depth=4, seed=seed)
    params = pqc.parameters
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    par2val = dict(zip(params, values))
    qiskit_circ = pqc.assign_parameters(par2val)
    arr1 = Operator(qiskit_circ).data
    symb_op = symb_Operator(pqc)
    arr2 = symb_op.to_lambda()(*values)
    assert numpy.allclose(arr1, arr2)
