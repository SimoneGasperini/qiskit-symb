"""Test standard gates module"""

import numpy
from qiskit.circuit.library import (
    IGate,
    XGate,
    YGate,
    ZGate,
    HGate,
    SXGate,
    SXdgGate,
    SGate,
    SdgGate,
    TGate,
    TdgGate,
    SwapGate,
    iSwapGate,
    DCXGate,
    ECRGate,
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
    DCXGate as symb_DCXGate,
    ECRGate as symb_ECRGate,
)


def convert_endian(unitary):
    """todo"""
    nq = int(numpy.log2(len(unitary)))
    perm = [int(bin(i)[2:].zfill(nq)[::-1], 2) for i in range(len(unitary))]
    return unitary[numpy.ix_(perm, perm)]


def test_id():
    """todo"""
    arr1 = IGate().to_matrix()
    arr2 = symb_IGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_x():
    """todo"""
    arr1 = XGate().to_matrix()
    arr2 = symb_XGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_y():
    """todo"""
    arr1 = YGate().to_matrix()
    arr2 = symb_YGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_z():
    """todo"""
    arr1 = ZGate().to_matrix()
    arr2 = symb_ZGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_h():
    """todo"""
    arr1 = HGate().to_matrix()
    arr2 = symb_HGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_sx():
    """todo"""
    arr1 = SXGate().to_matrix()
    arr2 = symb_SXGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_sxdg():
    """todo"""
    arr1 = SXdgGate().to_matrix()
    arr2 = symb_SXdgGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_s():
    """todo"""
    arr1 = SGate().to_matrix()
    arr2 = symb_SGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_sdg():
    """todo"""
    arr1 = SdgGate().to_matrix()
    arr2 = symb_SdgGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_t():
    """todo"""
    arr1 = TGate().to_matrix()
    arr2 = symb_TGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_tdg():
    """todo"""
    arr1 = TdgGate().to_matrix()
    arr2 = symb_TdgGate(0).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_swap():
    """todo"""
    arr1 = convert_endian(SwapGate().to_matrix())
    arr2 = symb_SwapGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_iswap():
    """todo"""
    arr1 = convert_endian(iSwapGate().to_matrix())
    arr2 = symb_iSwapGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_dcx():
    """todo"""
    arr1 = convert_endian(DCXGate().to_matrix())
    arr2 = symb_DCXGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_ecr():
    """todo"""
    arr1 = convert_endian(ECRGate().to_matrix())
    arr2 = symb_ECRGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)
