# -*- coding: utf-8 -*-
# @Time    : 2022/11/25 11:34
# @Author  : Walter
# @File    : Python 计算字典值之和.py
# @License : (C)Copyright Walter
# @Desc    :
def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum


dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))