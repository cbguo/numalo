#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : template.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#


# include_packages
from typing import List, Callable

# description
""" 

计算元素的排列  

"""

# code
"""
def permute(nums: List[int]) -> List[List[int]]:
    pass
"""


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) < 2:
        return [nums.copy()]
    result = list()
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute(nums)
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)

    return result


# test
def test():
    print("Permutation: ")
    for nums in [
        [1],
        [1, 2, 3],
        [2, 1, 3],
        [3, 2, 4, 5]
    ]:
        print(f"nums: {nums}, \n\tres: {permute(nums)}")

    pass


# main
if __name__ == '__main__':
    print(permute([1]))
    print(permute([1, 2]))
