"""Symbolic random module"""

import random
from qiskit import QuantumRegister, QuantumCircuit
from qiskit.circuit import ParameterVector, Qubit
from qiskit.circuit.library import standard_gates


def random_parametric_circuit(num_qubits, depth, seed=None):
    """todo"""
    # pylint: disable=too-many-locals
    register = QuantumRegister(num_qubits)
    circuit = QuantumCircuit(register)
    if num_qubits == 0 or depth == 0:
        return circuit
    qiskit_gates = {
        # gate_name: (gate_class, num_qubits, num_params)
        'id': (standard_gates.IGate, 1, 0),
        'sx': (standard_gates.SXGate, 1, 0),
        'x': (standard_gates.XGate, 1, 0),
        'rz': (standard_gates.RZGate, 1, 1),
        'r': (standard_gates.RGate, 1, 2),
        'h': (standard_gates.HGate, 1, 0),
        'p': (standard_gates.PhaseGate, 1, 1),
        'rx': (standard_gates.RXGate, 1, 1),
        'ry': (standard_gates.RYGate, 1, 1),
        's': (standard_gates.SGate, 1, 0),
        'sdg': (standard_gates.SdgGate, 1, 0),
        'sxdg': (standard_gates.SXdgGate, 1, 0),
        't': (standard_gates.TGate, 1, 0),
        'tdg': (standard_gates.TdgGate, 1, 0),
        'u': (standard_gates.UGate, 1, 3),
        'y': (standard_gates.YGate, 1, 0),
        'z': (standard_gates.ZGate, 1, 0),
    }
    if num_qubits > 1:
        qiskit_gates.update({
            'cx': (standard_gates.CXGate, 2, 0),
            # 'dcx': (standard_gates.DCXGate, 2, 0), TODO
            'ch': (standard_gates.CHGate, 2, 0),
            'cp': (standard_gates.CPhaseGate, 2, 1),
            'crx': (standard_gates.CRXGate, 2, 1),
            'cry': (standard_gates.CRYGate, 2, 1),
            'crz': (standard_gates.CRZGate, 2, 1),
            'csx': (standard_gates.CSXGate, 2, 0),
            # https://github.com/Qiskit/qiskit-terra/issues/7326
            # 'cu': (standard_gates.CUGate, 2, 4),
            'cy': (standard_gates.CYGate, 2, 0),
            'cz': (standard_gates.CZGate, 2, 0),
            'rxx': (standard_gates.RXXGate, 2, 1),
            'ryy': (standard_gates.RYYGate, 2, 1),
            'rzz': (standard_gates.RZZGate, 2, 1),
            'rzx': (standard_gates.RZXGate, 2, 1),
            # 'xx_minus_yy': (standard_gates.XXMinusYYGate, 2, 2), TODO
            # 'xx_plus_yy': (standard_gates.XXPlusYYGate, 2, 2), TODO
            'ecr': (standard_gates.ECRGate, 2, 0),
            'cs': (standard_gates.CSGate, 2, 0),
            'csdg': (standard_gates.CSdgGate, 2, 0),
            'swap': (standard_gates.SwapGate, 2, 0),
            'iswap': (standard_gates.iSwapGate, 2, 0)
        })
    random.seed(seed)
    qiskit_gates_names = list(qiskit_gates.keys())
    params = ParameterVector(name='x', length=0)
    while circuit.depth() != depth:
        gate_name = random.choice(qiskit_gates_names)
        gate_init, n_qubits, n_params = qiskit_gates[gate_name]
        length = len(params)
        params.resize(length + n_params)
        gate = gate_init(*params[length:])
        indices = list(range(num_qubits))
        qubits = [Qubit(register=register,
                        index=indices.pop(random.randrange(len(indices))))
                  for _ in range(n_qubits)]
        circuit.append(instruction=gate, qargs=qubits)
    return circuit
