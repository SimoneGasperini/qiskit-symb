"""Test standard gates module"""

import numpy
from hypothesis import given, strategies, settings
from qiskit.quantum_info import random_unitary
from qiskit.circuit.library import (
    IGate, XGate, YGate, ZGate,
    HGate, SXGate, SXdgGate,
    SGate, SdgGate, TGate, TdgGate,
    SwapGate, iSwapGate,
    ECRGate, DCXGate,
    UnitaryGate
)
from qiskit_symb.circuit.library import (
    IGate as symb_IGate,
    XGate as symb_XGate,
    YGate as symb_YGate,
    ZGate as symb_ZGate,
    HGate as symb_HGate,
    SXGate as symb_SXGate,
    SXdgGate as symb_SXdgGate,
    SGate as symb_SGate,
    SdgGate as symb_SdgGate,
    TGate as symb_TGate,
    TdgGate as symb_TdgGate,
    SwapGate as symb_SwapGate,
    iSwapGate as symb_iSwapGate,
    ECRGate as symb_ECRGate,
    DCXGate as symb_DCXGate,
    UnitaryGate as symb_UnitaryGate
)


def test_id():
    """todo"""
    arr1 = IGate().to_matrix()
    arr2 = symb_IGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_x():
    """todo"""
    arr1 = XGate().to_matrix()
    arr2 = symb_XGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_y():
    """todo"""
    arr1 = YGate().to_matrix()
    arr2 = symb_YGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_z():
    """todo"""
    arr1 = ZGate().to_matrix()
    arr2 = symb_ZGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_h():
    """todo"""
    arr1 = HGate().to_matrix()
    arr2 = symb_HGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_sx():
    """todo"""
    arr1 = SXGate().to_matrix()
    arr2 = symb_SXGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_sxdg():
    """todo"""
    arr1 = SXdgGate().to_matrix()
    arr2 = symb_SXdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_s():
    """todo"""
    arr1 = SGate().to_matrix()
    arr2 = symb_SGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_sdg():
    """todo"""
    arr1 = SdgGate().to_matrix()
    arr2 = symb_SdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_t():
    """todo"""
    arr1 = TGate().to_matrix()
    arr2 = symb_TGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_tdg():
    """todo"""
    arr1 = TdgGate().to_matrix()
    arr2 = symb_TdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_swap():
    """todo"""
    arr1 = SwapGate().to_matrix()
    arr2 = symb_SwapGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_iswap():
    """todo"""
    arr1 = iSwapGate().to_matrix()
    arr2 = symb_iSwapGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ecr():
    """todo"""
    arr1 = ECRGate().to_matrix()
    arr2 = symb_ECRGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_dcx():
    """todo"""
    arr1 = DCXGate().to_matrix()
    arr2 = symb_DCXGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(min_value=1, max_value=2))
def test_unitary(num_qubits):
    """todo"""
    unitary = random_unitary(dims=2**num_qubits).data
    arr1 = UnitaryGate(unitary).to_matrix()
    arr2 = symb_UnitaryGate(unitary).to_numpy()
    assert numpy.allclose(arr1, arr2)
