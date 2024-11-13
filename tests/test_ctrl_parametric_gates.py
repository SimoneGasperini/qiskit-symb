"""Test controlled parametric gates module"""

import numpy
from hypothesis import given, strategies
from qiskit.circuit import ParameterVector, Parameter
from qiskit.circuit.library import (
    CUGate,
    U1Gate,
    U2Gate,
    U3Gate,
    CRXGate,
    CRYGate,
    CRZGate,
    CPhaseGate,
    RGate,
)
from qiskit_symb.circuit.library import (
    CUGate as symb_CUGate,
    CU1Gate as symb_CU1Gate,
    CU2Gate as symb_CU2Gate,
    CU3Gate as symb_CU3Gate,
    CRXGate as symb_CRXGate,
    CRYGate as symb_CRYGate,
    CRZGate as symb_CRZGate,
    CPhaseGate as symb_CPhaseGate,
    CRGate as symb_CRGate,
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
    gate = symb_CUGate(*pars, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(lam=strategies.floats(**val_range))
def test_cu1(lam):
    """todo"""
    par = Parameter(name='par')
    arr1 = U1Gate(lam).control(annotated=True).to_matrix()
    gate = symb_CU1Gate(par, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: lam})
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range))
def test_cu2(phi, lam):
    """todo"""
    pars_vals = [phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = U2Gate(*pars_vals).control(annotated=True).to_matrix()
    gate = symb_CU2Gate(*pars, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range))
def test_cu3(theta, phi, lam):
    """todo"""
    pars_vals = [theta, phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = U3Gate(*pars_vals).control(annotated=True).to_matrix()
    gate = symb_CU3Gate(*pars, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_crx(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = CRXGate(theta).to_matrix()
    gate = symb_CRXGate(par, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cry(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = CRYGate(theta).to_matrix()
    gate = symb_CRYGate(par, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range))
def test_crz(phi):
    """todo"""
    par = Parameter(name='par')
    arr1 = CRZGate(phi).to_matrix()
    gate = symb_CRZGate(par, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: phi})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cp(theta):
    """todo"""
    par = Parameter(name='par')
    arr1 = CPhaseGate(theta).to_matrix()
    gate = symb_CPhaseGate(par, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),)
def test_cr(theta, phi):
    """todo"""
    pars_vals = [theta, phi]
    pars = ParameterVector(name='pars', length=len(pars_vals))
    arr1 = RGate(*pars_vals).control(annotated=True).to_matrix()
    gate = symb_CRGate(*pars, control=0, target=1)
    arr2 = gate.get_numpy_repr(nqubits=2, par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)
