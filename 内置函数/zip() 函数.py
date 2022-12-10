# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 1:17
# @Author  : Walter
# @File    : zip() 函数.py
# @License : (C)Copyright Walter
# @Desc    : zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。

'''
我们可以使用 list() 转换来输出列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
语法
zip([iterable, ...])
参数说明：
iterabl -- 一个或多个迭代器;
返回值
返回一个对象。
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
# 返回一个对象
zipped = zip(a, b)
print(zipped)
# list() 转换为列表
print(list(zipped))
# 元素个数与最短的列表一致
print(list(zip(a, c)))
# 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
a1, a2 = zip(*zip(a, b))
print(list(a1))
print(list(a2))
