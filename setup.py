import os

from glob import glob
from os.path import (
    basename,
    splitext,
)

from setuptools import setup, find_packages


NAME = 'shaper_dominos'
DESCRIPTION = 'Printable shaper fiducials for use with the Shaper Origin'
URL = "https://github.com/augiev/Shaper-Dominos"
LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
AUTHOR = 'https://github.com/augiev'


setup(
    name=NAME,
    version='0.0.1',
    packages=['shaper_dominos'],
    # metadata for upload to PyPI
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['svgwrite'],
)
