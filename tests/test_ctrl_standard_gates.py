"""Test controlled standard gates module"""

import numpy
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit_symbolic.library import (
    CXGate as symb_CXGate,
    CYGate as symb_CYGate,
    CZGate as symb_CZGate,
    CHGate as symb_CHGate,
    CSGate as symb_CSGate,
    CSdgGate as symb_CSdgGate
)


def test_cx():
    """todo"""
    circ = QuantumCircuit(2)
    circ.cx(0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CXGate(circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix()
    assert numpy.allclose(arr1, arr2)


def test_cy():
    """todo"""
    circ = QuantumCircuit(2)
    circ.cy(0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CYGate(circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix()
    assert numpy.allclose(arr1, arr2)


def test_cz():
    """todo"""
    circ = QuantumCircuit(2)
    circ.cz(0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CZGate(circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix()
    assert numpy.allclose(arr1, arr2)


def test_ch():
    """todo"""
    circ = QuantumCircuit(2)
    circ.ch(0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CHGate(circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix()
    assert numpy.allclose(arr1, arr2)


def test_cs():
    """todo"""
    circ = QuantumCircuit(2)
    circ.cs(0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CSGate(circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix()
    assert numpy.allclose(arr1, arr2)


def test_csdg():
    """todo"""
    circ = QuantumCircuit(2)
    circ.csdg(0, 1)
    arr1 = Operator(circ).data
    symb_gate = symb_CSdgGate(circ[0].qubits[0], circ[0].qubits[1])
    arr2 = symb_gate.to_matrix()
    assert numpy.allclose(arr1, arr2)
