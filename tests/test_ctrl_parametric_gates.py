"""Test controlled parametric gates module"""

import numpy
from hypothesis import given, strategies, settings
from qiskit.circuit import ParameterVector, Parameter
from qiskit.quantum_info import Operator
from qiskit.circuit.library import (
    UGate, RXGate, RYGate, RZGate,
    PhaseGate, RGate,
    RXXGate, RYYGate,
    RZZGate, RZXGate
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
    try:
        arr1 = Operator(circuit.assign_parameters(pars_vals)).data
    except TypeError:
        # https://github.com/Qiskit/qiskit-terra/issues/10002
        return
    arr2 = symb_Operator(
        circuit).subs({pars: pars_vals}).to_numpy()
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
    circuit = get_random_controlled(base_gate=RZGate(par), seed=seed)
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
    try:
        arr1 = Operator(circuit.assign_parameters(pars_vals)).data
    except TypeError:
        # https://github.com/Qiskit/qiskit-terra/issues/10002
        return
    arr2 = symb_Operator(
        circuit).subs({pars: pars_vals}).to_numpy()
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
        # https://github.com/Qiskit/qiskit-terra/issues/10311
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
        # https://github.com/Qiskit/qiskit-terra/issues/10311
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
        # https://github.com/Qiskit/qiskit-terra/issues/10311
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
        # https://github.com/Qiskit/qiskit-terra/issues/10311
        return
    arr1 = Operator(circuit.assign_parameters([theta])).data
    arr2 = symb_Operator(circuit).subs({par: theta}).to_numpy()
    assert numpy.allclose(arr1, arr2)
