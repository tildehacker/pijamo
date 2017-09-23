#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='PIJAMO',
    version='0.1.0',
    description="PIJAMO Is Just Another Music Organizer",
    long_description=open('README.md').read(),
    keywords="music organizer mutagen",
    packages=['pijamo'],
    install_requires=['mutagen'],
    extras_require={
        'dev': ['pep8'],
    },
)
