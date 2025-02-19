# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import os
import pathlib
from setuptools import setup
from setuptools import find_packages

VERSION = "0.0.1"

def get_requirements():
    with open("./requirements.txt") as reqsf:
        reqs = reqsf.readlines()
    return reqs

def get_readme_description(path: str = os.path.join(os.getcwd(), 'README.md')):
    """
    Get long description from readme file.
    """
    path = pathlib.Path(path).expanduser().resolve()
    with open(path, encoding='utf-8') as file:
        description = file.read()

if __name__ == "__main__":
    setup(
        name="jepa",
        packages=find_packages(),
        version=VERSION,
        description="JEPA research code.",
        long_description=get_readme_description(),
        long_description_content_type='text/markdown',
        python_requires=">=3.9",
        install_requires=get_requirements(),
        url='https://github.com/tien-ngnvan/jepa',
    )
