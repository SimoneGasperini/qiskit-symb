"""Test density matrix module"""

import numpy
import pytest
from qiskit.quantum_info import DensityMatrix
from qiskit_symb.circuit.random import random_parametric_circuit
from qiskit_symb.quantum_info import DensityMatrix as symb_DensityMatrix
from qiskit_symb.utils import get_random_params


# pylint: disable=duplicate-code
testing_params = {'num_qubits': (1, 3), 'seed': (0, 999)}
pars, ids = get_random_params(testing_params, size=10)


@pytest.fixture(scope='module', params=pars, ids=ids)
def _test_data(request):
    """todo"""
    num_qubits, seed = request.param
    circuit = random_parametric_circuit(num_qubits, depth=4, seed=seed)
    symb_rho = symb_DensityMatrix(circuit)
    return circuit, symb_rho


def test_from_circuit(_test_data):
    """todo"""
    circuit, symb_rho = _test_data
    params = circuit.parameters
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    params_dict = dict(zip(params, values))
    qiskit_circ = circuit.assign_parameters(params_dict)
    arr1 = DensityMatrix(qiskit_circ).data
    arr2 = symb_rho.subs(params_dict).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_to_lambda(_test_data):
    """todo"""
    circuit, symb_rho = _test_data
    params = circuit.parameters
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    qiskit_circ = circuit.assign_parameters(values)
    arr1 = DensityMatrix(qiskit_circ).data
    arr2 = symb_rho.to_lambda()(*values)
    assert numpy.allclose(arr1, arr2)
