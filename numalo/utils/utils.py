#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : utils.py
# @Author    : Bangguo Chen
# @Email     : mail@cbguo.com
# @Demand    : 
# @Solution  : 
#


__all__ = [
    "decorator_check",
]

import os
import sys
from typing import Callable


def decorator_check(cls=None, method=None, check_funcs=None):
    def func1(decorator_func):
        _method1 = method

        def func2(method=None, *args, **kws):
            _method = None
            if method is None:
                _method = _method1
                if cls is not None:
                    c = cls()
                    _method = getattr(c, _method)
                _method = _method if isinstance(_method,
                                                Callable) else globals().get(
                    _method, lambda x: None)
                _check_funcs = check_funcs
                _check_funcs = [] if _check_funcs is None else _check_funcs
                for func in _check_funcs:
                    func(_method)
            else:
                _method = method if isinstance(method,
                                               Callable) else globals().get(
                    method, lambda x: None)

            decorator_func(_method, *args, **kws)

        return func2

    return func1
