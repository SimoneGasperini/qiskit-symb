"""Python package installer"""

import setuptools


with open('requirements.txt', encoding='utf-8') as file:
    install_requires = file.read()

setuptools.setup(
    name='qiskit-symbolic',
    version='0.0.1',
    url='https://github.com/SimoneGasperini/qiskit-symbolic',
    author='SimoneGasperini',
    author_email='simone.gasperini4@unibo.it',
    license='Apache 2.0',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    python_requires='>=3.8'
)
