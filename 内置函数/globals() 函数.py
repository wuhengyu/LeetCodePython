# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 1:09
# @Author  : Walter
# @File    : globals() 函数.py
# @License : (C)Copyright Walter
# @Desc    : globals() 函数会以字典类型返回当前位置的全部全局变量。
'''
参数
无
返回值
返回全局变量的字典。
'''
a = 'runoob'
# globals 函数返回一个全局变量的字典，包括所有导入的变量。
print(globals())
