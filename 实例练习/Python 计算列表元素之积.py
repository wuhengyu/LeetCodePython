# -*- coding: utf-8 -*-
# @Time    : 2022/11/25 11:34
# @Author  : Walter
# @File    : Python 计算列表元素之积.py
# @License : (C)Copyright Walter
# @Desc    :
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))