#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests'
]

test_requirements = requirements + [
    # TODO: put package test requirements here
]

setup(
    name='pysia',
    version='0.1.0',
    description="Sia bindings for Python 2 & 3",
    long_description=readme + '\n\n' + history,
    author="Jeffrey McLarty",
    author_email='jeffrey.mclarty@gmail.com',
    url='https://github.com/jnmclarty/pysia',
    packages=[
        'pysia',
    ],
    package_dir={'pysia':
                 'pysia'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pysia',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
