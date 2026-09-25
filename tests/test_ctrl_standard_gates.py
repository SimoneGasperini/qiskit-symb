"""Test controlled standard gates module"""

import numpy
from qiskit.circuit.library import (
    CHGate,
    CSdgGate,
    CSGate,
    CSXGate,
    CXGate,
    CYGate,
    CZGate,
    SXdgGate,
    TdgGate,
    TGate,
)

from qiskit_symb.circuit.library import (
    CHGate as symb_CHGate,
)
from qiskit_symb.circuit.library import (
    CSdgGate as symb_CSdgGate,
)
from qiskit_symb.circuit.library import (
    CSGate as symb_CSGate,
)
from qiskit_symb.circuit.library import (
    CSXdgGate as symb_CSXdgGate,
)
from qiskit_symb.circuit.library import (
    CSXGate as symb_CSXGate,
)
from qiskit_symb.circuit.library import (
    CTdgGate as symb_CTdgGate,
)
from qiskit_symb.circuit.library import (
    CTGate as symb_CTGate,
)
from qiskit_symb.circuit.library import (
    CXGate as symb_CXGate,
)
from qiskit_symb.circuit.library import (
    CYGate as symb_CYGate,
)
from qiskit_symb.circuit.library import (
    CZGate as symb_CZGate,
)


def convert_endian(unitary):
    """todo"""
    unitary = numpy.asarray(unitary)
    nq = int(numpy.log2(len(unitary)))
    perm = [int(bin(i)[2:].zfill(nq)[::-1], 2) for i in range(len(unitary))]
    return unitary[numpy.ix_(perm, perm)]


def test_cx():
    """todo"""
    arr1 = convert_endian(CXGate().to_matrix())
    arr2 = symb_CXGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_cy():
    """todo"""
    arr1 = convert_endian(CYGate().to_matrix())
    arr2 = symb_CYGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_cz():
    """todo"""
    arr1 = convert_endian(CZGate().to_matrix())
    arr2 = symb_CZGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_ch():
    """todo"""
    arr1 = convert_endian(CHGate().to_matrix())
    arr2 = symb_CHGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_csx():
    """todo"""
    arr1 = convert_endian(CSXGate().to_matrix())
    arr2 = symb_CSXGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_csxdg():
    """todo"""
    arr1 = convert_endian(SXdgGate().control(annotated=True).to_matrix().data)
    arr2 = symb_CSXdgGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_cs():
    """todo"""
    arr1 = convert_endian(convert_endian(CSGate().to_matrix()))
    arr2 = symb_CSGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_csdg():
    """todo"""
    arr1 = convert_endian(CSdgGate().to_matrix())
    arr2 = symb_CSdgGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_ct():
    """todo"""
    arr1 = convert_endian(TGate().control(annotated=True).to_matrix().data)
    arr2 = symb_CTGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)


def test_ctdg():
    """todo"""
    arr1 = convert_endian(TdgGate().control(annotated=True).to_matrix().data)
    arr2 = symb_CTdgGate(0, 1).get_numpy_repr()
    assert numpy.allclose(arr1, arr2)
