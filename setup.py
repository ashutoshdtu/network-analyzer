from setuptools import setup
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='network-analyzer',
    version="0.0.1",
    author="Ashutosh Mishra <ashutoshdtu@gmail.com>, Saurabh Shandilya <saurabhshandilya.1991@gmail.com>",
    author_email="ashutoshdtu@gmail.com, saurabhshandilya.1991@gmail.com",
    description="Analyze your network traffic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashutoshdtu/network-analyzer",
    packages=['network_analyzer', 'rpc_apiserver', 'socketio_server'],
    include_package_data=True,
    install_requires=required,
)