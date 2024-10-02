"""Test controlled standard gates module"""

import numpy
from qiskit.circuit.library import (
    CXGate,
    CYGate,
    CZGate,
    CHGate,
    CSXGate,
    SXdgGate,
    CSGate,
    CSdgGate,
    TGate,
    TdgGate,
    CSwapGate,
    iSwapGate,
)
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
    CiSwapGate as symb_CiSwapGate,
)


def test_cx():
    """todo"""
    arr1 = CXGate().to_matrix()
    arr2 = symb_CXGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cy():
    """todo"""
    arr1 = CYGate().to_matrix()
    arr2 = symb_CYGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cz():
    """todo"""
    arr1 = CZGate().to_matrix()
    arr2 = symb_CZGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ch():
    """todo"""
    arr1 = CHGate().to_matrix()
    arr2 = symb_CHGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_csx():
    """todo"""
    arr1 = CSXGate().to_matrix()
    arr2 = symb_CSXGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_csxdg():
    """todo"""
    arr1 = SXdgGate().control(annotated=True).to_matrix()
    arr2 = symb_CSXdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cs():
    """todo"""
    arr1 = CSGate().to_matrix()
    arr2 = symb_CSGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_csdg():
    """todo"""
    arr1 = CSdgGate().to_matrix()
    arr2 = symb_CSdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ct():
    """todo"""
    arr1 = TGate().control(annotated=True).to_matrix()
    arr2 = symb_CTGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ctdg():
    """todo"""
    arr1 = TdgGate().control(annotated=True).to_matrix()
    arr2 = symb_CTdgGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_cswap():
    """todo"""
    arr1 = CSwapGate().to_matrix()
    arr2 = symb_CSwapGate().to_numpy()
    assert numpy.allclose(arr1, arr2)


def test_ciswap():
    """todo"""
    arr1 = iSwapGate().control(annotated=True).to_matrix()
    arr2 = symb_CiSwapGate().to_numpy()
    assert numpy.allclose(arr1, arr2)
