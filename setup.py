#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import sys
#from . import tests


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='tagweed',
    version='0.1.0',
    description='tagweed provides help in cleaning up tag clouds such as those seen in pinboard.io, delicious.com, etc',
    long_description=readme + '\n\n' + history,
    author='Richard Shea',
    author_email='rshea@thecubagroup.com',
    url='https://github.com/shearichard/tagweed',
    packages=[
        'tagweed',
    ],
    package_dir={'tagweed': 'tagweed'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='tagweed',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
