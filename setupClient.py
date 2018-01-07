from setuptools import setup, find_packages
import os.path

import sys

__version__ = '2.2.1'

descr_file = os.path.join(os.path.dirname(__file__), 'README.rst')

if sys.version_info > (3, 0):
    requirements = [
        'requests'
    ]
else:
    requirements = [
        'requests',
        'mock'
    ]

setup(
    name='sarasensei',
    version=__version__,

    packages=find_packages(exclude=['test']),

    description='My league private server',
    long_description=open(descr_file).read(),
    author='Sara',
    url='https://github.com/SaraSensei',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'Topic :: Games/Entertainment :: Role-Playing'
    ],
    license='MIT',
    install_requires=requirements,
 )
-ñ