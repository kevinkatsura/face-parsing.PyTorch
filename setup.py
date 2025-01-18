from distutils.core import setup
from setuptools import find_packages

setup(
    name='face-parsing', 
    version='1.0.0',
    package_dir= {
        "face_parsing" : ".",
        "face_parsing.modules": "modules/"
    })

# packages=find_packages(where=".", exclude=["makeup"])