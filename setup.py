#!/usr/bin/env python
# Read the LICENSE file in the root folder

from setuptools import setup, find_packages
# from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='dirsch',
    version='0.1.0',
    description='',
    # long_description=long_description,
    url='',
    author='Kevin Robertson',
    author_email='kevin_robertson+dirsch@stemulator.org',
    license='Public Domain',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['doc', 'test']),
    install_requires=[],
    package_data={},
    data_files=[],
)
