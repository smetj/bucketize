#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py
#
#  Copyright 2016 Jelle Smet <development@smetj.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

PROJECT = 'bucketize'
VERSION = '0.1.0'

install_requires = [
]

dependency_links = [
]

try:
    with open('README.rst', 'rt') as f:
        long_description = f.read()
except IOError:
    long_description = ''


setup(
    name=PROJECT,
    version=VERSION,

    description='A CLI tool to determine STDIN line rate at the interval of choice.',
    long_description=long_description,

    author='Jelle Smet',
    author_email='development@smetj.net',

    url='https://github.com/smetj/bucketize',
    download_url='https://github.com/smetj/bucketize/tarball/master',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: Implementation :: PyPy',
                 'Intended Audience :: System Administrators',
                 ],
    platforms=['Linux'],
    install_requires=install_requires,
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': ['bucketize = bucketize:main'],
    }
)
