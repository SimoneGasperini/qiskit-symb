"""Test controlled standard gates module"""

import numpy
from hypothesis import given, strategies, settings
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit.circuit.library import (
    XGate, CXGate,
    YGate, CYGate,
    ZGate, CZGate,
    HGate, CHGate,
    SXGate, CSXGate,
    SXdgGate,
    SGate, CSGate,
    SdgGate, CSdgGate,
    TGate,
    TdgGate,
    SwapGate, CSwapGate,
    iSwapGate
)
from qiskit_symb.utils import get_random_controlled
from qiskit_symb import Operator as symb_Operator
from qiskit_symb.circuit.library import (
    CXGate as symb_CXGate,
    CYGate as symb_CYGate,
    CZGate as symb_CZGate,
    CHGate as symb_CHGate,
    CSXGate as symb_CSXGate,
    CSXdgGate as symb_CSXdgGate,
    CSGate as symb_CSGate,
    CSdgGate as symb_CSdgGate,
    CTGate as symb_CTGate,
    CTdgGate as symb_CTdgGate,
    CSwapGate as symb_CSwapGate,
    CiSwapGate as symb_CiSwapGate
)


def test_cx():
    """todo"""
    arr1 = CXGate().to_matrix()
    arr2 = symb_CXGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mcx(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=XGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cy():
    """todo"""
    arr1 = CYGate().to_matrix()
    arr2 = symb_CYGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mcy(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=YGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cz():
    """todo"""
    arr1 = CZGate().to_matrix()
    arr2 = symb_CZGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mcz(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=ZGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ch():
    """todo"""
    arr1 = CHGate().to_matrix()
    arr2 = symb_CHGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mch(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=HGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_csx():
    """todo"""
    arr1 = CSXGate().to_matrix()
    arr2 = symb_CSXGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mcsx(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SXGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_csxdg():
    """todo"""
    circuit = QuantumCircuit(2)
    circuit.append(SXdgGate().control(), qargs=[0, 1])
    arr1 = Operator(circuit).data
    arr2 = symb_CSXdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mcsxdg(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SXdgGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cs():
    """todo"""
    arr1 = CSGate().to_matrix()
    arr2 = symb_CSGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mcs(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_csdg():
    """todo"""
    arr1 = CSdgGate().to_matrix()
    arr2 = symb_CSdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mcsdg(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SdgGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ct():
    """todo"""
    circuit = QuantumCircuit(2)
    circuit.append(TGate().control(), qargs=[0, 1])
    arr1 = Operator(circuit).data
    arr2 = symb_CTGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mct(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=TGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ctdg():
    """todo"""
    circuit = QuantumCircuit(2)
    circuit.append(TdgGate().control(), qargs=[0, 1])
    arr1 = Operator(circuit).data
    arr2 = symb_CTdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mctdg(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=TdgGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cswap():
    """todo"""
    arr1 = CSwapGate().to_matrix()
    arr2 = symb_CSwapGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mcswap(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=SwapGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ciswap():
    """todo"""
    circuit = QuantumCircuit(3)
    circuit.append(iSwapGate().control(), qargs=[0, 1, 2])
    arr1 = Operator(circuit).data
    arr2 = symb_CiSwapGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None, max_examples=10)
@given(seed=strategies.integers(min_value=0))
def test_mciswap(seed):
    """todo"""
    circuit = get_random_controlled(base_gate=iSwapGate(), seed=seed)
    arr1 = Operator(circuit).data
    arr2 = symb_Operator(circuit).to_numpy()
    assert numpy.allclose(arr1, arr2)
