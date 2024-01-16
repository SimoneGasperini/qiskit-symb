"""Test controlled standard gates module"""

import numpy
from hypothesis import given, strategies, settings

from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit.circuit.library import (
    XGate, YGate, ZGate,
    HGate, SXGate, SXdgGate,
    SGate, SdgGate, TGate, TdgGate,
    SwapGate, iSwapGate, ECRGate, CZGate, CXGate, CSXGate
)
from qiskit.transpiler.passes import Unroller
from qiskit_symb.utils import get_random_controlled
from qiskit_symb import Operator as symb_Operator


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_cx(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=XGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_cy(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=YGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_cz(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=ZGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)
@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_ccz(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=CZGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)

@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_ccx(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=CXGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)

@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_rccx(seed):
    """todo"""
    qc = QuantumCircuit(4)
    qc.rccx(0, 1, 2)
    qc2 = Unroller(basis=['cx', 'u1', 'u2'])(qc)
    arr1 = Operator(qc2).data
    arr2 = symb_Operator(qc2).to_numpy()
    assert numpy.allclose(arr1, arr2)

@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_rcccx(seed):
    """todo"""
    qc = QuantumCircuit(4)
    qc.rcccx(0, 1, 2, 3)
    qc2 = Unroller(basis=['cx', 'u1', 'u2'])(qc)
    arr1 = Operator(qc2).data
    arr2 = symb_Operator(qc2).to_numpy()
    assert numpy.allclose(arr1, arr2)

@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_ch(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=HGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_csx(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SXGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)

@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_c2sx(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=CSXGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)

@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_c3sx(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=CSXGate().control(1), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)

@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_csxdg(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SXdgGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_cs(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_csdg(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SdgGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_ct(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=TGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_ctdg(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=TdgGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_cswap(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SwapGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_ciswap(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=iSwapGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_cecr(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=ECRGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)
