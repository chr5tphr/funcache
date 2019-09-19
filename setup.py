#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name = "funcache",
    version = "0.1",
    packages=find_packages(),
    install_requires=[
        'metrohash-python>=1.13.post2',
    ],
    extra_require={
        'torch': ['torch>=1.2.0'],
        'numpy': ['numpy>=1.17.2'],
    }
)
