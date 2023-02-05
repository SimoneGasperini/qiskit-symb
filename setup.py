import setuptools


with open('requirements.txt', encoding='utf-8') as file:
    install_requires = file.read()

setuptools.setup(
    packages=setuptools.find_packages(),
    install_requires=install_requires
)
