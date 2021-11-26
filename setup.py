#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python setup.py sdist bdist_wheel
# twine upload dist/*
# twine upload --skip-existing dist/*

from setuptools import setup, find_packages

import ritl

setup(
    name='ritl',
    version=ritl.__version__,
    packages=find_packages(),
    author="Guitheg",
    description="Relatives Import Tool",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='https://github.com/Guitheg/ritl',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Education",
    ],
    license="MIT", 
)