# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 13:15
# @Author  : Walter
# @File    : 斐波那契数列3.py
# @License : (C)Copyright Walter
# @Desc    : 输出指定个数的斐波那契数列

# 斐波那契数列
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
# 输出前10个斐波那契数列
print(fib(10))
