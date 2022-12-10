# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 21:22
# @Author  : Walter
# @File    : eval() 函数.py
# @License : (C)Copyright Walter
# @Desc    : eval() 函数用来执行一个字符串表达式，并返回表达式的值。

'''
参数
expression -- 表达式。
globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
'''

x = 7
print(eval('3 * x'))
print(eval('pow(2,2)'))
print(eval('2 + 2'))
n = 81
print(eval("n + 4"))
