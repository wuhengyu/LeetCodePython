# -*- coding: utf-8 -*-
# @Time    : 2022/11/25 15:03
# @Author  : Walter
# @File    : Python 移除列表中重复的元素.py
# @License : (C)Copyright Walter
# @Desc    :

# 首先将列表转换为集合，然后再次将其转换为列表。集合中不能有重复元素，因此 set() 会删除重复的元素
list_1 = [1, 2, 1, 4, 6]
print(list(set(list_1)))


# set()将两个列表转换为两个集合，用于删除列表中的重复元素
# ^ 运算符得到两个列表的对称差

list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))