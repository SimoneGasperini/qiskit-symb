"""Test statevector module"""

import numpy
from hypothesis import given, strategies, settings
from qiskit.quantum_info import Statevector
from qiskit_symb.quantum_info import Statevector as symb_Statevector
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
    arr1 = Statevector(qiskit_circ).data
    symb_psi = symb_Statevector.from_circuit(pqc)
    arr2 = symb_psi.subs(par2val).to_numpy()[:, 0]
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
    arr1 = Statevector(qiskit_circ).data
    symb_psi = symb_Statevector(pqc)
    arr2 = symb_psi.to_lambda()(*values)[:, 0]
    assert numpy.allclose(arr1, arr2)
