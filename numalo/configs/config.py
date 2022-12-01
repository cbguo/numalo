#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : config.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#


__all__ = [
    "cfg"
]

import os
import sys
from pathlib import Path

class Config:
    def __init__(self):
        file = Path(__file__)
        self.DIR_PATH_PROJECT = str(file.parents[2])
        self.DIR_PATH_PACKAGE = str(file.parents[1])
        self.PATH_CODES_TEMPLATE = os.path.join(
            self.DIR_PATH_PACKAGE, "codes", "template.py"
        )


cfg = Config()
