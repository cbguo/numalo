#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : py_template.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#

import os
import argparse
import numpy as np

from numalo.codes.structs import CodeTemp
from numalo.configs import cfg


def py_template_empty():
    parser = argparse.ArgumentParser(
        usage="numalo.py_template",
        description="生成一个空的py模板",
    )
    parser.add_argument(
        "dst", type=str, default=f"template.py",
        help="The path to save the template. "
    )

    args = parser.parse_args()

    ct = CodeTemp()
    ct.load(os.path.join(cfg.PATH_CODES_TEMPLATE))
    ct.dump(args.dst)


def py_template():
    parser = argparse.ArgumentParser(
        usage="numalo.py_template_empty",
        description="生成一个py code 模板",
    )
    parser.add_argument(
        "src", type=str,
        help="输入的源py文件, 用于生成模板"
    )
    parser.add_argument(
        "--dst", type=str, default="template-empty.py",
        help="生成的空模板路径"
    )
    args = parser.parse_args()
    assert os.path.isfile(args.src)

    ct = CodeTemp()
    ct.load(args.src)
    ct.dump(args.dst)
