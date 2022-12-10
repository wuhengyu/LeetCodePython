# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 0:27
# @Author  : Walter
# @File    : staticmethod() 函数.py
# @License : (C)Copyright Walter
# @Desc    : python staticmethod 返回函数的静态方法。
'''
该方法不强制要求传递参数
'''

class C(object):
    @staticmethod
    def f():
        print('runoob')


# 静态方法无需实例化
C.f()
# 也可以实例化后调用
C().f()