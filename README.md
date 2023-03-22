![logo](/img/logo.png)

<p align="center">
    <img title="license" src="https://img.shields.io/badge/license-Apache_2.0-blue.svg">
    <img title="python" src="https://img.shields.io/badge/python-≥3.8-blue.svg">
</p>

<p align="center">
    <img title="test" src='https://github.com/SimoneGasperini/qiskit-symbolic/actions/workflows/test.yml/badge.svg?branch=master'>
    <img title="lint" src='https://github.com/SimoneGasperini/qiskit-symbolic/actions/workflows/lint.yml/badge.svg?branch=master'>
    <img title="coverage" src='https://coveralls.io/repos/github/SimoneGasperini/qiskit-symbolic/badge.svg?branch=master'>
</p>

***

# Table of contents
- [Introduction](#introduction)
- [Installation](#installation)
    - [User-mode](#user-mode)
    - [Dev-mode](#dev-mode)
- [How to use?](#how-to-use)


# Introduction
The `qiskit-symbolic` package is meant to be a Python tool to enable the symbolic evaluation of parametric quantum states and operators defined in [Qiskit](https://github.com/Qiskit/qiskit-terra) by parameterized quantum circuits.

A Parameterized Quantum Circuit (PQC) is a quantum circuit where we have at least one free parameter (e.g. a rotation angle $\theta$). PQCs are particularly relevant in Quantum Machine Learning (QML) models, where the values of these parameters can be learned during training to reach the desired output.

In particular, `qiskit-symbolic` can be used to create a symbolic representation of a parametric quantum statevector, density matrix, or unitary operator directly from the Qiskit quantum circuit. This has been achieved through the re-implementation of some basic classes defined in the [`qiskit/quantum_info/`](https://github.com/Qiskit/qiskit-terra/tree/main/qiskit/quantum_info) module by using [sympy](https://github.com/sympy/sympy) as a backend for symbolic expressions manipulation.


# Installation
### User-mode
To start using `qiskit-symbolic`, you can install the package directly from GitHub running the following command:
```
pip install git+https://github.com/SimoneGasperini/qiskit-symbolic.git
```
### Dev-mode
To install the package in development mode, first you have to clone locally the GitHub repository; then, move to the repo directory to install the develop dependencies and to launch the editable-mode installation running the following commands:
```
pip install -r requirements-dev.txt
pip install -e .
```


# How to use?
To show a simple example on how to use `qiskit-symbolic`, consider the following PQC defined in Qiskit:
```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

y = Parameter('y')
p = ParameterVector('p', length=2)

qc = QuantumCircuit(2)
qc.ry(y, 0)
qc.cx(0, 1)
qc.u(0, *p, 1)

qc.draw('mpl')
```
![example](/img/example.png)

To get the symbolic matrix representation of the parametric unitary operator corresponding to the circuit, the following few lines of code are enough:
```python
from qiskit_symbolic import Operator

op = Operator.from_circuit(qc)
op.to_sympy()
```
```math
\left[\begin{matrix}\cos{\left(\frac{y}{2} \right)} & - \sin{\left(\frac{y}{2} \right)} & 0 & 0\\0 & 0 & \sin{\left(\frac{y}{2} \right)} & \cos{\left(\frac{y}{2} \right)}\\0 & 0 & e^{i \left(p[0] + p[1]\right)} \cos{\left(\frac{y}{2} \right)} & - e^{i \left(p[0] + p[1]\right)} \sin{\left(\frac{y}{2} \right)}\\e^{i \left(p[0] + p[1]\right)} \sin{\left(\frac{y}{2} \right)} & e^{i \left(p[0] + p[1]\right)} \cos{\left(\frac{y}{2} \right)} & 0 & 0\end{matrix}\right]
```

If you want to assign a value to some specific parameter, you can use the `Operator.subs` method passing a dictionary that maps each parameter to its corresponding value:
```python
params2value = {p: [-1, 2]}
new_op = op.subs(params2value)
new_op.to_sympy()
```
```math
\left[\begin{matrix}\cos{\left(\frac{y}{2} \right)} & - \sin{\left(\frac{y}{2} \right)} & 0 & 0\\0 & 0 & \sin{\left(\frac{y}{2} \right)} & \cos{\left(\frac{y}{2} \right)}\\0 & 0 & e^{i} \cos{\left(\frac{y}{2} \right)} & - e^{i} \sin{\left(\frac{y}{2} \right)}\\e^{i} \sin{\left(\frac{y}{2} \right)} & e^{i} \cos{\left(\frac{y}{2} \right)} & 0 & 0\end{matrix}\right]
```

***

<p align="right">
    <img src="https://avatars2.githubusercontent.com/u/71086758?s=400&v=4" width="80px"/><br>
    <b>Simone Gasperini</b><br>
    <a href="https://github.com/SimoneGasperini">GitHub</a>,
    <a href="https://www.unibo.it/sitoweb/simone.gasperini4">UniBo</a>
</p>