"""Test parametric gates module"""

import numpy
from hypothesis import given, strategies
from qiskit.circuit import ParameterVector, Parameter
from qiskit.circuit.library import (
    UGate, RXGate, RYGate, RZGate,
    PhaseGate, RGate,
    RXXGate, RYYGate,
    RZZGate, RZXGate
)
from qiskit_symb.circuit.library import (
    UGate as symb_UGate,
    RXGate as symb_RXGate,
    RYGate as symb_RYGate,
    RZGate as symb_RZGate,
    PhaseGate as symb_PhaseGate,
    RGate as symb_RGate,
    RXXGate as symb_RXXGate,
    RYYGate as symb_RYYGate,
    RZZGate as symb_RZZGate,
    RZXGate as symb_RZXGate
)

val_range = {'min_value': -2*numpy.pi, 'max_value': 2*numpy.pi}


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range))
def test_u(theta, phi, lam):
    """todo"""
    pars_vals = [theta, phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = UGate(*pars_vals).to_matrix()
    arr2 = symb_UGate(*pars).to_numpy(*pars_vals)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_rx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RXGate(theta).to_matrix()
    arr2 = symb_RXGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_ry(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RYGate(theta).to_matrix()
    arr2 = symb_RYGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range))
def test_rz(phi):
    """todo"""
    par = Parameter(name='par')
    arr1 = RZGate(phi).to_matrix()
    arr2 = symb_RZGate(par).to_numpy(phi)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_p(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = PhaseGate(theta).to_matrix()
    arr2 = symb_PhaseGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range))
def test_r(theta, phi):
    """todo"""
    pars_vals = [theta, phi]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = RGate(*pars_vals).to_matrix()
    arr2 = symb_RGate(*pars).to_numpy(*pars_vals)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_rxx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RXXGate(theta).to_matrix()
    arr2 = symb_RXXGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_ryy(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RYYGate(theta).to_matrix()
    arr2 = symb_RYYGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_rzz(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RZZGate(theta).to_matrix()
    arr2 = symb_RZZGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_rzx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RZXGate(theta).to_matrix()
    arr2 = symb_RZXGate(par).to_numpy(theta)
    assert numpy.allclose(arr1, arr2)
