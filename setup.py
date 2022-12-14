"""Setup for the npdocval package."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import versioneer


README_RST = ''
with open('README.rst', encoding="utf-8") as f:
    README_RST = f.read()

INSTALL_REQUIRES = [
    'numpy',
]
TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov', 'pytest-ordering',
    # to be able to run `python setup.py checkdocs`
    'collective.checkdocs', 'pygments',
]


setup(
    name='npdocval',
    description="Numpy docstring validation CLI",
    long_description=README_RST,
    long_description_content_type='text/x-rst',
    author="Shay Palachy",
    author_email="shaypal5@gmail.com",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/shaypal5/numpydoc-validate',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES
    },
    platforms=['any'],
    keywords='pandas dataframe pipeline data',
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
