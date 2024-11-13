"""Test parametric gates module"""

import numpy
from hypothesis import given, strategies
from qiskit.circuit import ParameterVector, Parameter
from qiskit.circuit.library import (
    UGate,
    U1Gate,
    U2Gate,
    U3Gate,
    RXGate,
    RYGate,
    RZGate,
    PhaseGate,
    RGate,
    RXXGate,
    RYYGate,
    RZZGate,
    RZXGate,
    XXMinusYYGate,
    XXPlusYYGate,
)
from qiskit_symb.circuit.library import (
    UGate as symb_UGate,
    U1Gate as symb_U1Gate,
    U2Gate as symb_U2Gate,
    U3Gate as symb_U3Gate,
    RXGate as symb_RXGate,
    RYGate as symb_RYGate,
    RZGate as symb_RZGate,
    PhaseGate as symb_PhaseGate,
    RGate as symb_RGate,
    RXXGate as symb_RXXGate,
    RYYGate as symb_RYYGate,
    RZZGate as symb_RZZGate,
    RZXGate as symb_RZXGate,
    XXMinusYYGate as symb_XXMinusYYGate,
    XXPlusYYGate as symb_XXPlusYYGate,
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


@given(lam=strategies.floats(**val_range))
def test_u1(lam):
    """todo"""
    par = Parameter(name='par')
    arr1 = U1Gate(lam).to_matrix()
    gate = symb_U1Gate(par, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val={par: lam})
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range))
def test_u2(phi, lam):
    """todo"""
    pars_vals = [phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = U2Gate(*pars_vals).to_matrix()
    gate = symb_U2Gate(*pars, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range))
def test_u3(theta, phi, lam):
    """todo"""
    pars_vals = [theta, phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = U3Gate(*pars_vals).to_matrix()
    gate = symb_U3Gate(*pars, target=0)
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


@given(lam=strategies.floats(**val_range))
def test_p(lam):
    """todo"""
    par = Parameter(name='par')
    arr1 = PhaseGate(lam).to_matrix()
    gate = symb_PhaseGate(lam=par, target=0)
    arr2 = gate.get_numpy_repr(nqubits=1, par2val={par: lam})
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


@given(theta=strategies.floats(**val_range))
def test_rxx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RXXGate(theta).to_matrix()
    gate = symb_RXXGate(theta=par, target1=0, target2=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_ryy(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RYYGate(theta).to_matrix()
    gate = symb_RYYGate(theta=par, target1=0, target2=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_rzz(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RZZGate(theta).to_matrix()
    gate = symb_RZZGate(theta=par, target1=0, target2=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_rzx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = RZXGate(theta).to_matrix()
    gate = symb_RZXGate(theta=par, target1=0, target2=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range),
       beta=strategies.floats(**val_range))
def test_xx_minus_yy(theta, beta):
    """todo"""
    pars_vals = [theta, beta]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = XXMinusYYGate(*pars_vals).to_matrix()
    gate = symb_XXMinusYYGate(*pars, target1=0, target2=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range),
       beta=strategies.floats(**val_range))
def test_xx_plus_yy(theta, beta):
    """todo"""
    pars_vals = [theta, beta]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = XXPlusYYGate(*pars_vals).to_matrix()
    gate = symb_XXPlusYYGate(*pars, target1=0, target2=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)
