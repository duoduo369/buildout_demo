# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='buildout_demo',
    version='0.0.1',
    license='MIT',
    author='',
    author_email='',
    description='buildout demo',
    url='',
    packages=find_packages(exclude=['tests']),
    package_data={'buildout_demo': ['README.md']},
    package_dir={'': 'src'},
)
