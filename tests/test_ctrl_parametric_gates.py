"""Test controlled parametric gates module"""

import numpy
from hypothesis import given, strategies, settings
from qiskit.circuit import ParameterVector, Parameter
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit.circuit.library import (
    UGate, RXGate, RYGate, RZGate,
    PhaseGate, RGate
)
from qiskit_symbolic.utils import get_random_qubits
from qiskit_symbolic.circuit.library import (
    CUGate as symb_CUGate,
    CRXGate as symb_CRXGate,
    CRYGate as symb_CRYGate,
    CRZGate as symb_CRZGate,
    CPhaseGate as symb_CPhaseGate,
    CRGate as symb_CRGate
)

val_range = {'min_value': -2*numpy.pi, 'max_value': 2*numpy.pi}
qbits_range = {'min_value': 2, 'max_value': 4}


@settings(deadline=None)
@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range),
       num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_cu(theta, phi, lam, num_qubits, seed):
    """todo"""
    pars_vals = [theta, phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = UGate(*pars_vals).control(num_ctrl_qubits=len(ctrl_qubits),
                                          ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CUGate(*pars, ctrl_qubits, target_qubits,
                       ctrl_state).to_numpy(*pars_vals)
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(theta=strategies.floats(**val_range),
       num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_crx(theta, num_qubits, seed):
    """todo"""
    par = Parameter(name='par')
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = RXGate(theta).control(num_ctrl_qubits=len(ctrl_qubits),
                                      ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CRXGate(par, ctrl_qubits, target_qubits,
                        ctrl_state).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(theta=strategies.floats(**val_range),
       num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_cry(theta, num_qubits, seed):
    """todo"""
    par = Parameter(name='par')
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = RYGate(theta).control(num_ctrl_qubits=len(ctrl_qubits),
                                      ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CRYGate(par, ctrl_qubits, target_qubits,
                        ctrl_state).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(phi=strategies.floats(**val_range),
       num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_crz(phi, num_qubits, seed):
    """todo"""
    par = Parameter(name='par')
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = RZGate(phi).control(num_ctrl_qubits=len(ctrl_qubits),
                                    ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CRZGate(par, ctrl_qubits, target_qubits,
                        ctrl_state).to_numpy(phi)
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(theta=strategies.floats(**val_range),
       num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_cp(theta, num_qubits, seed):
    """todo"""
    par = Parameter(name='par')
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = PhaseGate(theta).control(num_ctrl_qubits=len(ctrl_qubits),
                                         ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CPhaseGate(par, ctrl_qubits, target_qubits,
                           ctrl_state).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_cr(theta, phi, num_qubits, seed):
    """todo"""
    pars_vals = [theta, phi]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = RGate(*pars_vals).control(num_ctrl_qubits=len(ctrl_qubits),
                                          ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CRGate(*pars, ctrl_qubits, target_qubits,
                       ctrl_state).to_numpy(*pars_vals)
    assert numpy.allclose(arr1, arr2)
