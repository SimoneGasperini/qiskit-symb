![](/img/logo.png)

<p align="center">
    <img title="license" src="https://img.shields.io/badge/license-Apache_2.0-blue.svg">
    <img title="python" src="https://img.shields.io/badge/python-≥3.8-blue.svg">
    <a href="https://qiskit.org/ecosystem/" alt="Ecosystem">
        <img src="https://img.shields.io/badge/Qiskit-Ecosystem-blueviolet.svg" /></a>
</p>

<p align="center">
    <img title="build" src='https://github.com/SimoneGasperini/qiskit-symb/actions/workflows/python-package.yml/badge.svg?branch=master'>
    <img title="coverage" src='https://coveralls.io/repos/github/SimoneGasperini/qiskit-symb/badge.svg?branch=master'>
</p>

***
This package was presented at [Qiskit DemoDays](https://github.com/Qiskit/feedback/wiki/Qiskit-DemoDays) on June 15th 2023 $\rightarrow$ [Webex recording](https://ibm.webex.com/recordingservice/sites/ibm/recording/playback/c6d96f25edba103bb7d600505681044d) (password: `Demoday20230615`) + [Jupyter notebook](https://github.com/Qiskit/feedback/blob/main/demo-day-notebooks/2023-06-15/1_qiskit_symb_demo.ipynb)
***

# Table of contents
- [Introduction](#introduction)
- [Installation](#installation)
    - [User-mode](#user-mode)
    - [Dev-mode](#dev-mode)
- [Usage examples](#usage-examples)
    - [_Sympify_ a Qiskit circuit](#sympify-a-qiskit-circuit)
    - [_Lambdify_ a Qiskit circuit](#lambdify-a-qiskit-circuit)
- [Contributors](#contributors)


# Introduction
The `qiskit-symb` package is meant to be a Python tool to enable the symbolic evaluation of parametric quantum states and operators defined in [Qiskit](https://github.com/Qiskit/qiskit-terra) by parameterized quantum circuits.

A Parameterized Quantum Circuit (PQC) is a quantum circuit where we have at least one free parameter (e.g. a rotation angle $\theta$). PQCs are particularly relevant in Quantum Machine Learning (QML) models, where the values of these parameters can be learned during training to reach the desired output.

In particular, `qiskit-symb` can be used to create a symbolic representation of a parametric quantum statevector, density matrix, or unitary operator directly from the Qiskit quantum circuit. This has been achieved through the re-implementation of some basic classes defined in the [`qiskit/quantum_info/`](https://github.com/Qiskit/qiskit-terra/tree/main/qiskit/quantum_info) module by using [sympy](https://github.com/sympy/sympy) as a backend for symbolic expressions manipulation.


# Installation

## User-mode
```
pip install qiskit-symb
```

## Dev-mode
```
git clone https://github.com/SimoneGasperini/qiskit-symb.git
cd qiskit-symb
pip install -e .
```


# Usage examples

### _Sympify_ a Qiskit circuit
Let's get started on how to use `qiskit-symb` to get the symbolic representation of a given Qiskit circuit. In particular, in this first basic example, we consider the following quantum circuit:
```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector

y = Parameter('y')
p = ParameterVector('p', length=2)

pqc = QuantumCircuit(2)
pqc.ry(y, 0)
pqc.cx(0, 1)
pqc.u(0, *p, 1)

pqc.draw('mpl')
```
![](/img/example_circuit.png)

To get the *sympy* representation of the unitary matrix corresponding to the parameterized circuit, we just have to create the symbolic `Operator` instance and call the `to_sympy()` method:
```python
from qiskit_symb.quantum_info import Operator

op = Operator(pqc)
op.to_sympy()
```
```math
\left[\begin{matrix}\cos{\left(\frac{y}{2} \right)} & - \sin{\left(\frac{y}{2} \right)} & 0 & 0\\0 & 0 & \sin{\left(\frac{y}{2} \right)} & \cos{\left(\frac{y}{2} \right)}\\0 & 0 & e^{i \left(p[0] + p[1]\right)} \cos{\left(\frac{y}{2} \right)} & - e^{i \left(p[0] + p[1]\right)} \sin{\left(\frac{y}{2} \right)}\\e^{i \left(p[0] + p[1]\right)} \sin{\left(\frac{y}{2} \right)} & e^{i \left(p[0] + p[1]\right)} \cos{\left(\frac{y}{2} \right)} & 0 & 0\end{matrix}\right]
```

If you want then to assign a value to some specific parameter, you can use the `subs(<dict>)` method passing a dictionary that maps each parameter to the desired corresponding value:
```python
new_op = op.subs({p: [-1, 2]})
new_op.to_sympy()
```
```math
\left[\begin{matrix}\cos{\left(\frac{y}{2} \right)} & - \sin{\left(\frac{y}{2} \right)} & 0 & 0\\0 & 0 & \sin{\left(\frac{y}{2} \right)} & \cos{\left(\frac{y}{2} \right)}\\0 & 0 & e^{i} \cos{\left(\frac{y}{2} \right)} & - e^{i} \sin{\left(\frac{y}{2} \right)}\\e^{i} \sin{\left(\frac{y}{2} \right)} & e^{i} \cos{\left(\frac{y}{2} \right)} & 0 & 0\end{matrix}\right]
```

### _Lambdify_ a Qiskit circuit
Given a Qiskit circuit, `qiskit-symb` also allows to generate a Python lambda function with actual arguments matching the Qiskit unbound parameters.
Let's consider the following example starting from a `ZZFeatureMap` circuit, commonly used as a data embedding ansatz in QML applications:
```python
from qiskit.circuit.library import ZZFeatureMap

pqc = ZZFeatureMap(feature_dimension=3, reps=1)
pqc.draw('mpl')
```
![](/img/zzfeaturemap_circuit.png)

To get the Python function representing the final parameteric statevector, we just have to create the symbolic `Statevector` instance and call the `to_lambda()` method:
```python
from qiskit_symb.quantum_info import Statevector

pqc = pqc.decompose()
statevec = Statevector(pqc).to_lambda()
```

We can now call the lambda-generated function `statevec` passing the `x` values we want to assign to each parameter. The returned object will be a *numpy* 2D-array (with `shape=(8,1)` in this case) representing the final output statevector `psi`.
```python
x = [1.24, 2.27, 0.29]
psi = statevec(*x)
```

This feature can be useful when, given a Qiskit PQC, we want to run it multiple times with different parameters values. Indeed, we can perform a single symbolic evalutation and then call the lambda generated function as many times as needed, passing different values of the parameters at each iteration.

# Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/SimoneGasperini"><img src="https://avatars2.githubusercontent.com/u/71086758?s=400&v=4" width="120px;"/><br/><b>Simone Gasperini</b></a></td>
  </tr>
</table>
