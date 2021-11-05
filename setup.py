from setuptools import setup, find_packages

from cmpda import PACKAGE_NAME, AUTHOR, DESCRIPTION, URL
from cmpda.__version__ import TAG

_LICENSE = 'GNU General Public License v3'
_PACKAGES = find_packages(exclude='Tests')
_CLASSIFIERS = []
_SCRIPTS = []

with open('requirements.txt', 'r') as f:
    _DEPENDENCIES = f.read().splitlines()

_KWARGS = dict(name=PACKAGE_NAME,
               version=TAG,
               author=AUTHOR,
               description=DESCRIPTION,
               license=_LICENSE,
               packages=_PACKAGES,
               include_package_data=True,
               url=URL,
               classifiers=_CLASSIFIERS,
               scripts=_SCRIPTS,
               install_requires=_DEPENDENCIES)


setup(**_KWARGS)
