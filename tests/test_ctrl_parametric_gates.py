"""Test controlled parametric gates module"""

import numpy
from hypothesis import given, strategies
from qiskit.circuit import ParameterVector, Parameter
from qiskit.circuit.library import (
    CUGate, CRXGate, CRYGate, CRZGate,
    CPhaseGate
)
from qiskit_symbolic.circuit.library import (
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
    arr1 = CUGate(*pars_vals).to_matrix()
    arr2 = symb_CUGate(*pars).to_numpy(*pars_vals)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_crx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = CRXGate(theta).to_matrix()
    arr2 = symb_CRXGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cry(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = CRYGate(theta).to_matrix()
    arr2 = symb_CRYGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range))
def test_crz(phi):
    """todo"""
    par = Parameter(name='par')
    arr1 = CRZGate(phi).to_matrix()
    arr2 = symb_CRZGate(par).to_numpy(phi)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cp(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = CPhaseGate(theta).to_matrix()
    arr2 = symb_CPhaseGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)
