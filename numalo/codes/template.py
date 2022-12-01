#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : template.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#


# include packages
from typing import List, Callable

# description
""" 

计算两数之和. 

"""

# code
"""
def add(a, b):
    pass 
"""


def add(a, b):
    return a + b


# test
def test():
    method = add
    assert method(1, 2) == 3
    assert method(3, 2) == 5
    pass


# __main__
if __name__ == '__main__':
    test()
    pass
