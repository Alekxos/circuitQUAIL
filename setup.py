import os, sys
from setuptools import setup, find_packages

setup(name='circuitq',
      version='1.2.1',
      description='Automated design of superconducting qubits',
      url='https://github.com/Alekxos/circuitQUAIL',
      author='Alekxos',
      author_email='boulton@stanford.edu',
      license='MIT',
      # packages=['circuitq']
      packages=find_packages(),
      install_requires= ['numpy', 'networkx', 'sympy', 'scipy', 'jax'],
      )

local_package_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(local_package_dir)
