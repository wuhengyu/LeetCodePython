# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 23:06
# @Author  : Walter
# @File    : reload() 函数.py
# @License : (C)Copyright Walter
# @Desc    : reload() 用于重新载入之前载入的模块。
'''
参数
module -- 模块对象。
返回值
返回模块对象。
'''

import sys, importlib
# 重新载入 sys 模块
print(importlib.reload(sys))