"""Test controlled parametric gates module"""

import numpy
from hypothesis import given, strategies, settings

from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector, Parameter
from qiskit.quantum_info import Operator
from qiskit.circuit.library import (
    UGate, RXGate, RYGate, RZGate,
    PhaseGate, RGate,
    RXXGate, RYYGate,
    RZZGate, RZXGate,
    XXMinusYYGate, XXPlusYYGate
)
from qiskit_symb.utils import get_random_controlled
from qiskit_symb import Operator as symb_Operator

val_range = {'min_value': -2*numpy.pi, 'max_value': 2*numpy.pi}


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_cu(theta, phi, lam, seed):
    """todo"""
    pars_vals = [theta, phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    circuit = get_random_controlled(base_gate=UGate(*pars), seed=seed)
    arr1 = Operator(circuit.assign_parameters(pars_vals)).data
    arr2 = symb_Operator(circuit).subs({pars: pars_vals}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_crx(theta, seed):
    """todo"""
    par = Parameter(name='par')
    circuit = get_random_controlled(base_gate=RXGate(par), seed=seed)
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_cry(theta, seed):
    """todo"""
    par = Parameter(name='par')
    circuit = get_random_controlled(base_gate=RYGate(par), seed=seed)
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(phi=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_crz(phi, seed):
    """todo"""
    par = Parameter(name='par')
    try:
        circuit = get_random_controlled(base_gate=RZGate(par), seed=seed)
    except TypeError:
        # https://github.com/Qiskit/qiskit/issues/10311
        return
    arr1 = Operator(circuit.assign_parameters([phi])).data
    arr2 = symb_Operator(circuit).subs({par: phi}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_cp(theta, seed):
    """todo"""
    par = Parameter(name='par')
    circuit = get_random_controlled(base_gate=PhaseGate(par), seed=seed)
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_cr(theta, phi, seed):
    """todo"""
    pars_vals = [theta, phi]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    circuit = get_random_controlled(base_gate=RGate(*pars), seed=seed)
    arr1 = Operator(circuit.assign_parameters(pars_vals)).data
    arr2 = symb_Operator(circuit).subs({pars: pars_vals}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_crxx(theta, seed):
    """todo"""
    par = Parameter(name='par')
    try:
        circuit = get_random_controlled(base_gate=RXXGate(par), seed=seed)
    except TypeError:
        # https://github.com/Qiskit/qiskit/issues/10311
        return
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_cryy(theta, seed):
    """todo"""
    par = Parameter(name='par')
    try:
        circuit = get_random_controlled(base_gate=RYYGate(par), seed=seed)
    except TypeError:
        # https://github.com/Qiskit/qiskit/issues/10311
        return
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_crzz(theta, seed):
    """todo"""
    par = Parameter(name='par')
    try:
        circuit = get_random_controlled(base_gate=RZZGate(par), seed=seed)
    except TypeError:
        # https://github.com/Qiskit/qiskit/issues/10311
        return
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range),
       seed=strategies.integers(min_value=0))
def test_crzx(theta, seed):
    """todo"""
    par = Parameter(name='par')
    try:
        circuit = get_random_controlled(base_gate=RZXGate(par), seed=seed)
    except TypeError:
        # https://github.com/Qiskit/qiskit/issues/10311
        return
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range))
def test_xx_minus_yy(theta):
    """todo"""
    par = Parameter(name='par')
    circuit = QuantumCircuit(2)
    circuit.append(XXMinusYYGate(par), (0, 1))
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(theta=strategies.floats(**val_range))
def test_xx_plus_yy(theta):
    """todo"""
    par = Parameter(name='par')
    circuit = QuantumCircuit(2)
    circuit.append(XXPlusYYGate(par), (0, 1))
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)
