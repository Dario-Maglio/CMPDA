from setuptools import setup, find_packages

from cmpda import PACKAGE_NAME, AUTHOR, DESCRIPTION, URL
from cmpda.__version__ import TAG

from pkg_resources import parse_version

#requirement to use the setup.cfg file during the setup
setuptools_version = parse_version(setuptools.__version__)
if setuptools_version < parse_version('39.2'):
    raise SystemExit('Please upgrade setuptools')

_LICENSE = 'GNU General Public License v3'
_PACKAGES = find_packages(exclude='Tests')
_CLASSIFIERS = ['Intended Audience :: Science/Research',
    'License :: OSI Approved :: '
    'GNU General Public License v3',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: C++',
    'Programming Language :: Fortran',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific computation',
    'Development Status :: Beta']
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
