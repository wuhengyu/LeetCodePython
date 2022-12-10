# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 23:20
# @Author  : Walter
# @File    : min() 函数.py
# @License : (C)Copyright Walter
# @Desc    : min() 方法返回给定参数的最小值，参数可以为序列。
'''
参数
x -- 数值表达式。
y -- 数值表达式。
z -- 数值表达式。

返回值
返回给定参数的最小值。
'''
print("min(80, 100, 1000) : ", min(80, 100, 1000))
print("min(-20, 100, 400) : ", min(-20, 100, 400))
print("min(-80, -20, -10) : ", min(-80, -20, -10))
print("min(0, 100, -400) : ", min(0, 100, -400))
print("min(0, 100, -400) : ", min([1, 2, 5, 8, 3]))
