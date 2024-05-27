#!/usr/bin/env python3

from setuptools import setup
from polite_lib.version import version

setup(
    name="polite-lib",
    description="Polite Lib",
    version=version,
    author="Alix",
    author_email="alix@politeauthority.io",
    packages=[
        "polite_lib",
        "polite_lib.utils",
        "polite_lib.file_tools",
        "polite_lib.fmt",
        "polite_lib.notify",
    ],
)

# End File: politeauthority/polite-lib/src/setup.py
