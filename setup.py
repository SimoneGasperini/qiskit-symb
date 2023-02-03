import setuptools


with open('requirements.txt') as file:
    install_requires = file.read()

setuptools.setup(
    name='qiskit-symbolic',
    author='SimoneGasperini',
    author_email='simone.gasperini4@unibo.it',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    python_requires='>=3.9'
)
