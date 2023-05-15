"""Test statevector module"""

import numpy
import pytest
from qiskit.quantum_info import Statevector
from qiskit_symb.circuit.random import random_parametric_circuit
from qiskit_symb.quantum_info import Statevector as symb_Statevector
from qiskit_symb.utils import get_random_params


# pylint: disable=duplicate-code
testing_params = {'num_qubits': (1, 3), 'seed': (0, 999)}
pars, ids = get_random_params(testing_params, size=10)


@pytest.fixture(scope='module', params=pars, ids=ids)
def _test_data(request):
    """todo"""
    num_qubits, seed = request.param
    circuit = random_parametric_circuit(num_qubits, depth=4, seed=seed)
    symb_psi = symb_Statevector(circuit)
    return circuit, symb_psi


def test_from_circuit(_test_data):
    """todo"""
    circuit, symb_psi = _test_data
    params = circuit.parameters
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    params_dict = dict(zip(params, values))
    qiskit_circ = circuit.assign_parameters(params_dict)
    arr1 = Statevector(qiskit_circ).data
    arr2 = symb_psi.subs(params_dict).to_numpy()[:, 0]
    assert numpy.allclose(arr1, arr2)


def test_to_lambda(_test_data):
    """todo"""
    circuit, symb_psi = _test_data
    params = circuit.parameters
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    qiskit_circ = circuit.assign_parameters(values)
    arr1 = Statevector(qiskit_circ).data
    arr2 = symb_psi.to_lambda()(*values)[:, 0]
    assert numpy.allclose(arr1, arr2)
