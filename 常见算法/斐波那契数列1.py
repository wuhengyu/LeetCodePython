# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 13:20
# @Author  : Walter
# @File    : 斐波那契数列1.py
# @License : (C)Copyright Walter
# @Desc    : 1、1、2、3、5、8、13、21、34、……

'''
F0 = 0 (n=0)
F1 = 1 (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''

# 斐波那契数列
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

print(fib(2))
# 输出了第10个斐波那契数列
print(fib(10))