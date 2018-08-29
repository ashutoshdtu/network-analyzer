from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='network-analyzer',
    packages=['network_analyzer'],
    include_package_data=True,
    install_requires=required,
)