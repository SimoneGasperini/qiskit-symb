<p align="center">
    <img src="https://github.com/SimoneGasperini/qiskit-symbolic/blob/master/logo.png">
</p>

<p align="center">
    <img title="license" src="https://img.shields.io/badge/license-Apache_2.0-blue.svg">
	<img title="python" src="https://img.shields.io/badge/python-≥3.8-blue.svg">
    <img title="build" src='https://github.com/SimoneGasperini/qiskit-symbolic/actions/workflows/testing.yml/badge.svg'>
</p>


## Table of contents
- [Introduction](#introduction)
- [Installation](#installation)

***


## Introduction
The `qiskit-symbolic` package is meant to be a Python tool to enable the symbolic evaluation of parametric quantum states and operators defined in [Qiskit](https://github.com/Qiskit/qiskit-terra) by parameterized quantum circuits.

A Parameterized Quantum Circuit (PQC) is a quantum circuit where we have at least one free parameter (e.g. a rotation angle $\theta$). PQCs are particularly relevant in Quantum Machine Learning (QML) models, where the values of these parameters can be learned during training to reach the desired output.

In particular, `qiskit-symbolic` can be used to create a symbolic representation of a parametric quantum statevector, density matrix, or unitary operator directly from the Qiskit quantum circuit. This has been achieved through the re-implementation of some basic classes defined in the [`qiskit/quantum_info/`](https://github.com/Qiskit/qiskit-terra/tree/main/qiskit/quantum_info) module by using [sympy](https://github.com/sympy/sympy) as a backend for symbolic expressions manipulation.


## Installation
To start using `qiskit-symbolic`, you can install the package directly from GitHub running the command:
```
pip install git+https://github.com/SimoneGasperini/qiskit-symbolic.git
```
To install the package from source in *dev-mode*, you have to clone the GitHub repository, install the develop dependencies, and run the installation in editable mode:
```
git clone https://github.com/SimoneGasperini/qiskit-symbolic.git
cd qiskit-symbolic
pip install -r requirements-dev.txt
pip install -e .
```