"""Test controlled parametric gates module"""

import numpy
from hypothesis import given, strategies
from qiskit.circuit import ParameterVector, Parameter
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit_symbolic.library import (
    CUGate as symb_CUGate,
    CRXGate as symb_CRXGate,
    CRYGate as symb_CRYGate,
    CRZGate as symb_CRZGate,
    CPhaseGate as symb_CPhaseGate,
)

val_range = {'min_value': -2*numpy.pi, 'max_value': 2*numpy.pi}


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range),
       gamma=strategies.floats(**val_range))
def test_cu(theta, phi, lam, gamma):
    """todo"""
    pars_vals = [theta, phi, lam, gamma]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    circ = QuantumCircuit(2)
    circ.cu(*pars_vals, 0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CUGate(*pars, circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix(pars_vals)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_crx(theta):
    """todo"""
    par = Parameter(name='par')
    circ = QuantumCircuit(2)
    circ.crx(theta, 0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CRXGate(par, circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cry(theta):
    """todo"""
    par = Parameter(name='par')
    circ = QuantumCircuit(2)
    circ.cry(theta, 0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CRYGate(par, circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix(theta)
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range))
def test_crz(phi):
    """todo"""
    par = Parameter(name='par')
    circ = QuantumCircuit(2)
    circ.crz(phi, 0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CRZGate(par, circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix(phi)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cp(theta):
    """todo"""
    par = Parameter(name='par')
    circ = QuantumCircuit(2)
    circ.cp(theta, 0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CPhaseGate(par, circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix(theta)
    assert numpy.allclose(arr1, arr2)
