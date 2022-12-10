# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 1:30
# @Author  : Walter
# @File    : hash() 函数.py
# @License : (C)Copyright Walter
# @Desc    : hash() 用于获取取一个对象（字符串或者数值等）的哈希值。
'''
语法
hash(object)
参数说明：
object -- 对象；
返回值
返回对象的哈希值。
'''
print(hash('test'))
print(hash(1))
print(hash(str([1, 2, 3])))
print(hash(str(sorted({'1': 1}))))
