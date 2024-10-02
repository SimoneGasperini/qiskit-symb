"""Test controlled parametric gates module"""

import numpy
from hypothesis import given, strategies
from qiskit.circuit import ParameterVector, Parameter
from qiskit.circuit.library import (
    CUGate,
    CRXGate,
    CRYGate,
    CRZGate,
    CPhaseGate,
    RGate,
    RXXGate,
    RYYGate,
    RZZGate,
    RZXGate,
)
from qiskit_symb.circuit.library import (
    CUGate as symb_CUGate,
    CRXGate as symb_CRXGate,
    CRYGate as symb_CRYGate,
    CRZGate as symb_CRZGate,
    CPhaseGate as symb_CPhaseGate,
    CRGate as symb_CRGate,
    CRXXGate as symb_CRXXGate,
    CRYYGate as symb_CRYYGate,
    CRZZGate as symb_CRZZGate,
    CRZXGate as symb_CRZXGate,
)

val_range = {'min_value': -2*numpy.pi, 'max_value': 2*numpy.pi}


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range))
def test_cu(theta, phi, lam):
    """todo"""
    pars_vals = [theta, phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = CUGate(*pars_vals, gamma=0).to_matrix()
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


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),)
def test_cr(theta, phi):
    """todo"""
    pars_vals = [theta, phi]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = RGate(*pars_vals).control(annotated=True).to_matrix()
    arr2 = symb_CRGate(*pars).to_numpy(*pars_vals)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_crxx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RXXGate(theta).control(annotated=True).to_matrix()
    arr2 = symb_CRXXGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cryy(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RYYGate(theta).control(annotated=True).to_matrix()
    arr2 = symb_CRYYGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_crzz(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RZZGate(theta).control(annotated=True).to_matrix()
    arr2 = symb_CRZZGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_crzx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RZXGate(theta).control(annotated=True).to_matrix()
    arr2 = symb_CRZXGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)
