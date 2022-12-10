# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 1:11
# @Author  : Walter
# @File    : map() 函数.py
# @License : (C)Copyright Walter
# @Desc    : map() 函数会根据提供的函数对指定序列做映射。
'''
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
语法
map(function, iterable, ...)
参数
function -- 函数
iterable -- 一个或多个序列
返回值
返回一个迭代器。
'''


def square(x):  # 计算平方数
    return x ** 2

# 计算列表各个元素的平方，返回迭代器map对象
print(map(square, [1, 2, 3, 4, 5]))
# 使用 list() 转换为列表
print(list(map(square, [1, 2, 3, 4, 5])))
# 使用 lambda 匿名函数
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
