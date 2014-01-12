import os
from setuptools import setup, find_packages
from distutils.core import setup
import py2exe

from pigeon_droppings import __version__

import pigeon_droppings

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = []

setup(
    name="Pigeon Droppings",
    version=".".join(map(str, __version__)),
    description="Utility that gets the DNS names of your aws instances based on the name you supply",
    long_description=read('README.rst'),
    url='',
    license='MIT',
    author='Jujhar Singh',
    author_email='jujhar@jujhar.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pd = pigeon_droppings.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=requirements,
    tests_require=[],
)
