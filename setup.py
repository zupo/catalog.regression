# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import find_packages
from setuptools import setup

import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

setup(
    name='catalog.regression',
    version=version,
    description="A buildout for finding out where the catalog regression occured.",
    long_description=read('docs', 'README.rst'),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Python',
    author='NiteoWeb Ltd.',
    author_email='info@niteoweb.com',
    url='http://www.niteoweb.com',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup', 'var']),
    namespace_packages=['catalog'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
        # list libs needed for unittesting this project
        'test': [
            'plone.app.testing',
            'unittest2',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
