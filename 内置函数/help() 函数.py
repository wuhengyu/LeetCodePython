# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 23:19
# @Author  : Walter
# @File    : help() 函数.py
# @License : (C)Copyright Walter
# @Desc    : help() 函数用于查看函数或模块用途的详细说明。
'''
参数：
object -- 对象
返回值:
返回对象帮助信息
'''

help('sys')  # 查看 sys 模块的帮助

help('str')  # 查看 str 数据类型的帮助

a = [1, 2, 3]
help(a)  # 查看列表 list 帮助信息

help(a.append)  # 显示list的append方法的帮助