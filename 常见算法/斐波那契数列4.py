# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 13:15
# @Author  : Walter
# @File    : 斐波那契数列4.py
# @License : (C)Copyright Walter
# @Desc    : 输出指定个数的斐波那契数列

# 斐波那契数列
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(11):
    print(fib(i))
