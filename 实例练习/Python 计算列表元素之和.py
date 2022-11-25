# -*- coding: utf-8 -*-
# @Time    : 2022/11/25 10:38
# @Author  : Walter
# @File    : Python 计算列表元素之和.py
# @License : (C)Copyright Walter
# @Desc    :

# 实例1
total = 0

list1 = [11, 5, 17, 18, 23]

for ele in range(0, len(list1)):
    total = total + list1[ele]

print("列表元素之和为: ", total)

# 实例2: 使用while () 循环
total = 0
ele = 0

list1 = [11, 5, 17, 18, 23]

while (ele < len(list1)):
    total = total + list1[ele]
    ele += 1

print("列表元素之和为: ", total)

# 实例3: 使用递归
list1 = [11, 5, 17, 18, 23]


def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


total = sumOfList(list1, len(list1))

print("列表元素之和为: ", total)