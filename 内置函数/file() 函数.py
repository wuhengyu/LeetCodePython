# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 20:45
# @Author  : Walter
# @File    : file() 函数.py
# @License : (C)Copyright Walter
# @Desc    : file() 函数用于创建一个 file 对象，它有一个别名叫 open()，更形象一些，它们是内置函数。参数是以字符串的形式传递的。

'''
参数：
name -- 文件名
mode -- 打开模式
buffering -- 0 表示不缓冲,如果为 1 表示进行行缓冲，大于 1 为缓冲区大小。

python默认的是gbk，而win10默认的是utf-8
Python3 已经没有这个file 内置函数
'''



f = open('test.txt', encoding='utf-8')
# print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())

print(f.readlines())
f.close()
