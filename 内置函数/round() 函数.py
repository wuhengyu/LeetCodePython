# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 1:14
# @Author  : Walter
# @File    : round() 函数.py
# @License : (C)Copyright Walter
# @Desc    : round() 方法返回浮点数 x 的四舍五入值，准确的说保留值将保留到离上一位更近的一端（四舍六入）。
'''
精度要求高的，不建议使用该函数。
语法
round( x [, n]  )
参数
x -- 数字表达式。
n -- 表示从小数点位数，其中 x 需要四舍五入，默认值为 0。
返回值
返回浮点数x的四舍五入值。
'''
print("round(70.23456) : ", round(70.23456))
print("round(56.659,1) : ", round(56.659, 1))
print("round(80.264, 2) : ", round(80.264, 2))
print("round(100.000056, 3) : ", round(100.000056, 3))
print("round(-100.000056, 3) : ", round(-100.000056, 3))
