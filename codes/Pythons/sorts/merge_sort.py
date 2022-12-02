#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : handle_template.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#


# include_packages
from typing import List, Callable
from numalo.codes.tests import sort_test

# description
""" 

This is a pure Python implementation of the merge sort algorithm.

"""

# code
"""
def merge_sort(nums: list) -> list:
    pass
"""


def merge_sort(nums: list) -> list:
    def merge(a, b):
        def _merge(a, b):
            while a and b:
                yield (a if a[0] < b[0] else b).pop(0)
            yield from a
            yield from b

        return list(_merge(a, b))

    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[0:mid]), merge_sort(nums[mid:]))

    pass


# test
def test():
    method = merge_sort
    assert method([2, 1, 3]) == [1, 2, 3]
    assert method([-5, 4, -2, -3, 0 - 6]) == [-6, -5, -3, -2, 4]
    sort_test(method)


# main
if __name__ == '__main__':
    test()
    pass
