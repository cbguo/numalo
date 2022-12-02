#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : setup.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#

import os
import re
from setuptools import setup, find_packages, find_namespace_packages

with open("numalo/__init__.py", "r") as f:
    data = f.read()
    _version = re.findall(r'__version__ = "([0-9.]+)"', data)[0]

packages = find_packages(
    where=".",
    exclude=(),
    include=("numalo*",)
)

setup(
    name="numalo",
    version=_version,
    description="This is a numalo learn package",
    author="cbguo",
    url="http://www.cbguo.com",
    packages=packages,
    entry_points={
        "console_scripts": [
            "numalo.py_template = numalo.scripts.templates.template:py_template",
            "numalo.py_template_empty = numalo.scripts.templates.template:py_template_empty",
        ]
    }
    # package_data={
    #     "lecode": [
    #         "untitled.md",
    #         "untitled.ipynb",
    #     ],
    # }
)
