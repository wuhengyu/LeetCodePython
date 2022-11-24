# -*- coding: utf-8 -*-
# @Time    : 2022/11/24 17:52
# @Author  : Walter
# @File    : Python 九九乘法表.py
# @License : (C)Copyright Walter
# @Desc    :

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()