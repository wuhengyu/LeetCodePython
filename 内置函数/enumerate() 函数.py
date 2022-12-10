# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 0:03
# @Author  : Walter
# @File    : enumerate() 函数.py
# @License : (C)Copyright Walter
# @Desc    : enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

'''
参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回值
返回 enumerate(枚举) 对象。
'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
# 小标从 1 开始
print(list(enumerate(seasons, start=1)))

# 普通的 for 循环
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1


# for 循环使用 enumerate
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)
