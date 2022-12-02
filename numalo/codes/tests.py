#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : tests.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#

__all__ = [
    "sort_test"
]

import os
import numpy as np
import random


def sort_test(func):
    for i in range(1000):
        nums = [random.randint(-500, 500) for i in range(i)]
        assert func(nums) == sorted(nums)
