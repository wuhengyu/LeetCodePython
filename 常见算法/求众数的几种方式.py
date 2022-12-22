# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 21:22
# @Author  : Walter
# @File    : 求众数的几种方式.py
# @License : (C)Copyright Walter
# @Desc    : Chatgpt

'''
注意：
如果输入的数据中有多个众数，上述代码只能返回其中一个。
如果输入的数据中没有众数（比如全部不同的数字），上述代码会返回最小的数字。
如果你想要更加精确地求众数，你可能需要使用更加复杂的算法。
'''

# 使用 collections.Counter 统计频率：
from collections import Counter


def mode(numbers):
    c = Counter(numbers)
    return c.most_common(1)[0][0]


print(mode([1, 2, 2, 3, 3, 3]))  # 3
print(mode([1, 1, 2, 3]))  # 1


# 使用字典统计频率：
def mode(numbers):
    count = {}
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    return max(count, key=count.get)


# 结论：
# 1、max() 函数中没有 key 参数时，求的是 key 的最大值
# 2、max() 函数中有 key 参数时，求的是 value 的最大值，但是函数返回的还是key
print(mode([1, 2, 2, 3, 3, 3, 3]))  # 3
print(mode([1, 1, 2, 3]))  # 1


# 使用集合去重后统计频率：
def mode(numbers):
    count = {}
    for number in set(numbers):
        count[number] = numbers.count(number)
    return max(count, key=count.get)


print(mode([1, 2, 2, 3, 3, 3]))  # 3
# print(mode([1, 1, 2, 3]))  # 1

# 使用 numpy 库：
import numpy as np


def mode(numbers):
    print(np.bincount(numbers))
    return np.bincount(numbers).argmax()


print(mode([1, 2, 2, 3, 3, 3]))  # 3
print(mode([1, 1, 2, 3]))  # 1
