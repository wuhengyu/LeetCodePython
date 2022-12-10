# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 23:22
# @Author  : Walter
# @File    : setattr() 函数.py
# @License : (C)Copyright Walter
# @Desc    : setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。

'''
参数
object -- 对象。
name -- 字符串，对象属性。
value -- 属性值。

返回值
无。
'''
# 对已存在的属性进行赋值：
class A(object):
    bar = 1
a = A()
print(a.bar)
getattr(a, 'bar')          # 获取属性 bar 值
setattr(a, 'bar', 5)       # 设置属性 bar 值
print(a.bar)

# 如果属性不存在会创建一个新的对象属性，并对属性赋值：
class A():
    name = "runoob"
a = A()
setattr(a, "age", 28)
print(a.age)