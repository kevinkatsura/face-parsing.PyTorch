from distutils.core import setup
from setuptools import find_packages

setup(
    name='face-parsing.PyTorch', 
    version='1.0.0', 
    packages=find_packages(
        where='/',
        # include=['pkg*'],  # alternatively: `exclude=['additional*']`
    ))