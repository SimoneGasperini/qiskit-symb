"""Test operator module"""

import numpy
import pytest
from qiskit.quantum_info import Operator
from qiskit_symbolic.circuit.random import random_parametric_circuit
from qiskit_symbolic.quantum_info import Operator as symb_Operator
from qiskit_symbolic.utils import get_random_params


# pylint: disable=duplicate-code
testing_params = {'num_qubits': (1, 3), 'seed': (0, 999)}
pars, ids = get_random_params(testing_params, size=10)


@pytest.fixture(scope='module', params=pars, ids=ids)
def _test_data(request):
    """todo"""
    num_qubits, seed = request.param
    circuit, params = random_parametric_circuit(
        num_qubits=num_qubits, depth=4, seed=seed)
    symb_op = symb_Operator(circuit)
    return circuit, params, symb_op


def test_from_circuit(_test_data):
    """todo"""
    circuit, params, symb_op = _test_data
    values = numpy.random.rand(len(params)) * 2*numpy.pi
    params_dict = dict(zip(params, values))
    qiskit_circ = circuit.assign_parameters(params_dict)
    arr1 = Operator(qiskit_circ).data
    arr2 = symb_op.subs(params_dict).to_numpy()
    assert numpy.allclose(arr1, arr2)
