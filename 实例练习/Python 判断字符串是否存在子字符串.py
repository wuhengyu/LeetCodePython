# -*- coding: utf-8 -*-
# @Time    : 2022/11/25 10:44
# @Author  : Walter
# @File    : Python 判断字符串是否存在子字符串.py
# @License : (C)Copyright Walter
# @Desc    : 给定一个字符串，然后判断指定的子字符串是否存在于该字符串中。

def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("不存在！")
    else:
        print("存在！")


string = "www.runoob.com"
sub_str = "runoob"
check(string, sub_str)