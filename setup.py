# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='godless',
    version='0.1.0',
    description='Game',
    long_description=readme,
    author='Karthik',
    author_email='kingomarigold@yahoo.com',
    url='https://github.com/kingomarigold/godless',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

