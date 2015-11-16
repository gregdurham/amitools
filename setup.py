# -*- coding: utf-8 -*-

import re
from setuptools import setup

requires = [
    'boto==2.5.2'
]

setup(
    name = "amitools",
    long_description=(
        '%s\n\n%s' % (
            open('README.md').read(),
            open('CHANGELOG.md').read()
        )
    ),
    package_dir={'amitools': 'src'},
    packages=["amitools",
              "amitools.lib"],
    scripts=["src/bin/amitools"],
    version=open('VERSION').read().strip(),
    description = "AMI tool kit for getting a tag for an instance ID",
    author = "Gregory Durham",
    author_email = "gregory.durham@gmail.com",
    include_package_data=True,
    install_requires=requires
    )
