# -*- coding: utf-8 -*-
# @Time    : 2022/12/19 10:29
# @Author  : Walter
# @File    : 列表寻找共同字符串.py
# @License : (C)Copyright Walter
# @Desc    :

strs = ['flower', 'flow', 'flight']
# 单个元素压缩
print(list(zip(strs)))
# 解压元素
print(list(zip(*strs)))
# 全部元素压缩
print(list(zip(*zip(strs))))
def search_str(self):
    re_data = ""
    for s in zip(*strs):
        if len(set(s))==1:
            re_data +=s[0]
        else:
            break
    return re_data
print(search_str(strs))