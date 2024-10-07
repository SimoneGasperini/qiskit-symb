"""Test parametric gates module"""

import numpy
from hypothesis import given, strategies
from qiskit.circuit import ParameterVector, Parameter
from qiskit.circuit.library import (
    UGate,
    RXGate,
    RYGate,
    RZGate,
    PhaseGate,
    RGate,
)
from qiskit_symb.circuit.library import (
    UGate as symb_UGate,
    RXGate as symb_RXGate,
    RYGate as symb_RYGate,
    RZGate as symb_RZGate,
    PhaseGate as symb_PhaseGate,
    RGate as symb_RGate,
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
    gate = symb_UGate(*pars, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_rx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RXGate(theta).to_matrix()
    gate = symb_RXGate(theta=par, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_ry(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RYGate(theta).to_matrix()
    gate = symb_RYGate(theta=par, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range))
def test_rz(phi):
    """todo"""
    par = Parameter(name='par')
    arr1 = RZGate(phi).to_matrix()
    gate = symb_RZGate(phi=par, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val={par: phi})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_p(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = PhaseGate(theta).to_matrix()
    gate = symb_PhaseGate(theta=par, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range))
def test_r(theta, phi):
    """todo"""
    pars_vals = [theta, phi]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = RGate(*pars_vals).to_matrix()
    gate = symb_RGate(*pars, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)
