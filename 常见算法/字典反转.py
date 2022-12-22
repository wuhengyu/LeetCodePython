# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 22:41
# @Author  : Walter
# @File    : 字典反转.py
# @License : (C)Copyright Walter
# @Desc    :
nums = {"a": 1, "b": 2, "c": 3, "d": 4}

print(dict(zip([i for i in nums.values()], [i for i in nums.keys()])))