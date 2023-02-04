"""Test standard gates module"""

import numpy
from sympy.utilities import lambdify
from qiskit.circuit import QuantumCircuit, ParameterVector, Parameter
from qiskit.quantum_info import Operator
from hypothesis import given, strategies
from qiskit_symbolic import GateSymb
from qiskit_symbolic.library import (
    UGateSymb,
    RXGateSymb,
    RYGateSymb,
    RZGateSymb
)

val_range = {'min_value': -2*numpy.pi, 'max_value': 2*numpy.pi}


@given(theta=strategies.floats(**val_range),
       phi=strategies.floats(**val_range),
       lam=strategies.floats(**val_range))
def test_u(theta, phi, lam):
    """todo"""
    circ = QuantumCircuit(1)
    pars_val = [theta, phi, lam]
    pars = ParameterVector(name='pars', length=len(pars_val))
    circ.u(*pars, 0)
    u_symb = GateSymb.from_instruction(circ.data[0])
    assert isinstance(u_symb, UGateSymb)
    ndarray1 = Operator(circ.assign_parameters({pars: pars_val})).data
    ndarray2 = lambdify(pars, u_symb.to_sympy(), 'numpy')(*pars_val)
    assert numpy.allclose(ndarray1, ndarray2)


@given(theta=strategies.floats(**val_range))
def test_rx(theta):
    """todo"""
    circ = QuantumCircuit(1)
    par = Parameter('par')
    circ.rx(par, 0)
    rx_symb = GateSymb.from_instruction(circ.data[0])
    assert isinstance(rx_symb, RXGateSymb)
    ndarray1 = Operator(circ.assign_parameters({par: theta})).data
    ndarray2 = lambdify([par], rx_symb.to_sympy(), 'numpy')(theta)
    assert numpy.allclose(ndarray1, ndarray2)


@given(theta=strategies.floats(**val_range))
def test_ry(theta):
    """todo"""
    circ = QuantumCircuit(1)
    par = Parameter('par')
    circ.ry(par, 0)
    ry_symb = GateSymb.from_instruction(circ.data[0])
    assert isinstance(ry_symb, RYGateSymb)
    ndarray1 = Operator(circ.assign_parameters({par: theta})).data
    ndarray2 = lambdify([par], ry_symb.to_sympy(), 'numpy')(theta)
    assert numpy.allclose(ndarray1, ndarray2)


@given(phi=strategies.floats(**val_range))
def test_rz(phi):
    """todo"""
    circ = QuantumCircuit(1)
    par = Parameter('par')
    circ.rz(par, 0)
    rz_symb = GateSymb.from_instruction(circ.data[0])
    assert isinstance(rz_symb, RZGateSymb)
    ndarray1 = Operator(circ.assign_parameters({par: phi})).data
    ndarray2 = lambdify([par], rz_symb.to_sympy(), 'numpy')(phi)
    assert numpy.allclose(ndarray1, ndarray2)
