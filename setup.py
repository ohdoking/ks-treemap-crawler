# -*- coding: utf-8 -*-

# Learn more: https://github.com/ohdoking/ks-treemap-crawler/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ks-treemap-crawler',
    version='0.0.1',
    description='kospi crawler',
    long_description=readme,
    author='Dokeun Oh',
    author_email='ohdoking@gmail.com',
    url='https://github.com/ohdoking/ks-treemap-crawler',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)