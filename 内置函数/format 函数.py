# -*- coding: utf-8 -*-
# @Time    : 2022/12/7 22:08
# @Author  : Walter
# @File    : format 格式化函数.py
# @License : (C)Copyright Walter
# @Desc    : Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能
'''
基本语法是通过 {} 和 : 来代替以前的 %
format 函数可以接受不限个参数，位置可以不按顺序。
'''
# 接受不限个参数，位置可以不按顺序
# 不设置指定位置，按默认顺序
print("{} {}".format("hello", "world"))
# 设置指定位置
print("{0} {1}".format("hello", "world"))
# 设置指定位置
print("{1} {0} {1}".format("hello", "world"))

# 也可以设置参数
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
# "0" 是必须的
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))

# 也可以向 str.format() 传入对象
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
# "0" 是可选的
# 向 str.format() 传入对象
print('value 为: {0.value}'.format(my_value))

# str.format()格式化数字的多种方法
# 保留小数点后两位
print("{:.2f}".format(3.1415926))
# 不带小数
print("{:.0f}".format(3.1415926))
# 带符号保留小数点后两位
print("{:+.2f}".format(3.1415926))
# 带符号保留小数点后两位
print("{:-.2f}".format(-1))
# 百分比格式
print("0.01的百分比表示：{:.0%}".format(0.01))
# 以逗号分隔的数字格式
print("{:,}".format(100000))
# 以十六进制表示
print("100的十六进制：{:#x}".format(100))
# 科学计数法表示
print("科学计数法：{:E}".format(1200.12))
# 进制
# 二进制、十进制、八进制、十六进制
print('{:b}'.format(11))
print('{:d}'.format(11))
print('{:o}'.format(11))
print('{:x}'.format(11))
print('{:#x}'.format(11))
print('{:#X}'.format(11))
# 大括号 {} 来转义大括号
print ("{} 对应的位置是 {{0}}".format("runoob"))