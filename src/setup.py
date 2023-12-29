#!/usr/bin/env python3

from setuptools import setup
version = "0.0.1"

setup(
    name="polite-lib",
    description="Polite Lib",
    version=version,
    author="Alix",
    author_email="alix@politeauthority.io",
    packages=[
        "polite_lib",
        "polite_lib.utils",
        "polite_lib.notify",
    ],
)

# End File: polite-lib/src/setup.py
