"""Symbolic controlled gate module"""

import sympy
from sympy.physics.quantum import TensorProduct
from .gate import Gate
from .state.statevector import Statevector


class ControlledGate(Gate):
    """Symbolic controlled gate base class"""

    projector_0 = Statevector.from_label('0').projector()
    projector_1 = Statevector.from_label('1').projector()

    def __init__(self, name, num_qubits, params,
                 control_qubit, target_qubit, base_gate, global_phase=False):
        """todo"""
        # pylint: disable=too-many-arguments
        super().__init__(name=name, num_qubits=num_qubits, params=params)
        self.control_qubit = control_qubit
        self.target_qubit = target_qubit
        self.base_gate = base_gate
        self.global_phase = global_phase

    @staticmethod
    def get(circuit_instruction):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=protected-access
        from .utils import get_init
        control_qubit = circuit_instruction.qubits[0]._index
        target_qubit = circuit_instruction.qubits[1]._index
        gate = circuit_instruction.operation
        return get_init(gate.name)(*gate.params, control_qubit, target_qubit)

    def __sympy__(self):
        """todo"""
        # pylint: disable=import-outside-toplevel
        # pylint: disable=no-member
        from .library.standard_gates import IGate
        from .utils import get_symbolic_expr
        imin = min(self.control_qubit, self.target_qubit)
        span = abs(self.control_qubit - self.target_qubit) + 1
        zero_term = [IGate().to_sympy()] * span
        zero_term[self.control_qubit - imin] = self.projector_0
        one_term = [IGate().to_sympy()] * span
        one_term[self.control_qubit - imin] = self.projector_1
        one_term[self.target_qubit - imin] = self.base_gate.__sympy__()
        gph = 1
        if self.global_phase:
            gamma = get_symbolic_expr(self.params[-1])
            gph = sympy.exp(sympy.I * gamma)
        return TensorProduct(*zero_term[::-1]) + gph * TensorProduct(*one_term[::-1])
