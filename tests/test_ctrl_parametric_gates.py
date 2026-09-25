"""Test controlled parametric gates module"""

import numpy
from hypothesis import given, strategies
from qiskit.circuit import Parameter, ParameterVector
from qiskit.circuit.library import (
    CPhaseGate,
    CRXGate,
    CRYGate,
    CRZGate,
    CUGate,
    RGate,
    U1Gate,
    U2Gate,
    U3Gate,
)

from qiskit_symb.circuit.library import (
    CPhaseGate as symb_CPhaseGate,
)
from qiskit_symb.circuit.library import (
    CRGate as symb_CRGate,
)
from qiskit_symb.circuit.library import (
    CRXGate as symb_CRXGate,
)
from qiskit_symb.circuit.library import (
    CRYGate as symb_CRYGate,
)
from qiskit_symb.circuit.library import (
    CRZGate as symb_CRZGate,
)
from qiskit_symb.circuit.library import (
    CU1Gate as symb_CU1Gate,
)
from qiskit_symb.circuit.library import (
    CU2Gate as symb_CU2Gate,
)
from qiskit_symb.circuit.library import (
    CU3Gate as symb_CU3Gate,
)
from qiskit_symb.circuit.library import (
    CUGate as symb_CUGate,
)


def convert_endian(unitary):
    """todo"""
    unitary = numpy.asarray(unitary)
    nq = int(numpy.log2(len(unitary)))
    perm = [int(bin(i)[2:].zfill(nq)[::-1], 2) for i in range(len(unitary))]
    return unitary[numpy.ix_(perm, perm)]


val_range = {"min_value": -2 * numpy.pi, "max_value": 2 * numpy.pi}


@given(
    theta=strategies.floats(**val_range),
    phi=strategies.floats(**val_range),
    lam=strategies.floats(**val_range),
    gamma=strategies.floats(**val_range),
)
def test_cu(theta, phi, lam, gamma):
    """todo"""
    pars_vals = [theta, phi, lam, gamma]
    pars = ParameterVector(name="pars", length=len(pars_vals))
    arr1 = convert_endian(CUGate(*pars_vals).to_matrix())
    gate = symb_CUGate(*pars, 0, 1)
    arr2 = gate.get_numpy_repr(par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(lam=strategies.floats(**val_range))
def test_cu1(lam):
    """todo"""
    par = Parameter(name="par")
    arr1 = convert_endian(U1Gate(lam).control(annotated=True).to_matrix().data)
    gate = symb_CU1Gate(par, 0, 1)
    arr2 = gate.get_numpy_repr(par2val={par: lam})
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range), lam=strategies.floats(**val_range))
def test_cu2(phi, lam):
    """todo"""
    pars_vals = [phi, lam]
    pars = ParameterVector(name="pars", length=len(pars_vals))
    arr1 = convert_endian(U2Gate(*pars_vals).control(annotated=True).to_matrix().data)
    gate = symb_CU2Gate(*pars, 0, 1)
    arr2 = gate.get_numpy_repr(par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(
    theta=strategies.floats(**val_range),
    phi=strategies.floats(**val_range),
    lam=strategies.floats(**val_range),
)
def test_cu3(theta, phi, lam):
    """todo"""
    pars_vals = [theta, phi, lam]
    pars = ParameterVector(name="pars", length=len(pars_vals))
    arr1 = convert_endian(U3Gate(*pars_vals).control(annotated=True).to_matrix().data)
    gate = symb_CU3Gate(*pars, 0, 1)
    arr2 = gate.get_numpy_repr(par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_crx(theta):
    """todo"""
    par = Parameter(name="par")
    arr1 = convert_endian(CRXGate(theta).to_matrix())
    gate = symb_CRXGate(par, 0, 1)
    arr2 = gate.get_numpy_repr(par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cry(theta):
    """todo"""
    par = Parameter(name="par")
    arr1 = convert_endian(CRYGate(theta).to_matrix())
    gate = symb_CRYGate(par, 0, 1)
    arr2 = gate.get_numpy_repr(par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(phi=strategies.floats(**val_range))
def test_crz(phi):
    """todo"""
    par = Parameter(name="par")
    arr1 = convert_endian(CRZGate(phi).to_matrix())
    gate = symb_CRZGate(par, 0, 1)
    arr2 = gate.get_numpy_repr(par2val={par: phi})
    assert numpy.allclose(arr1, arr2)


@given(theta=strategies.floats(**val_range))
def test_cp(theta):
    """todo"""
    par = Parameter(name="par")
    arr1 = convert_endian(CPhaseGate(theta).to_matrix())
    gate = symb_CPhaseGate(par, 0, 1)
    arr2 = gate.get_numpy_repr(par2val={par: theta})
    assert numpy.allclose(arr1, arr2)


@given(
    theta=strategies.floats(**val_range),
    phi=strategies.floats(**val_range),
)
def test_cr(theta, phi):
    """todo"""
    pars_vals = [theta, phi]
    pars = ParameterVector(name="pars", length=len(pars_vals))
    arr1 = convert_endian(RGate(*pars_vals).control(annotated=True).to_matrix().data)
    gate = symb_CRGate(*pars, 0, 1)
    arr2 = gate.get_numpy_repr(par2val=dict(zip(pars, pars_vals)))
    assert numpy.allclose(arr1, arr2)
