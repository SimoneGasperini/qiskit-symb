"""Test controlled standard gates module"""

import numpy
from hypothesis import given, strategies, settings
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit.circuit.library import (
    XGate, YGate, ZGate,
    HGate, SXGate, SXdgGate,
    SGate, SdgGate, TGate, TdgGate
)
from qiskit_symbolic.utils import get_random_qubits
from qiskit_symbolic.circuit.library import (
    CXGate as symb_CXGate,
    CYGate as symb_CYGate,
    CZGate as symb_CZGate,
    CHGate as symb_CHGate,
    CSXGate as symb_CSXGate,
    CSXdgGate as symb_CSXdgGate,
    CSGate as symb_CSGate,
    CSdgGate as symb_CSdgGate,
    CTGate as symb_CTGate,
    CTdgGate as symb_CTdgGate
)

qbits_range = {'min_value': 2, 'max_value': 4}


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_cx(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = XGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CXGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_cy(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = YGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CYGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_cz(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = ZGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CZGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_ch(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = HGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CHGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_csx(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = SXGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                 ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CSXGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_csxdg(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = SXdgGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                   ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CSXdgGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_cs(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = SGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CSGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_csdg(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = SdgGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                  ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CSdgGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_ct(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = TGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CTGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)


@settings(deadline=None)
@given(num_qubits=strategies.integers(**qbits_range),
       seed=strategies.integers(min_value=0))
def test_ctdg(num_qubits, seed):
    """todo"""
    ctrl_qubits, target_qubits, ctrl_state = \
        get_random_qubits(num_qubits=num_qubits, seed=seed)
    ctrl_gate = TdgGate().control(num_ctrl_qubits=len(ctrl_qubits),
                                  ctrl_state=ctrl_state)
    circuit = QuantumCircuit(num_qubits)
    circuit.append(ctrl_gate, ctrl_qubits+target_qubits)
    arr1 = Operator(circuit).data
    arr2 = symb_CTdgGate(ctrl_qubits, target_qubits, ctrl_state).to_numpy()
    assert numpy.allclose(arr1, arr2)
