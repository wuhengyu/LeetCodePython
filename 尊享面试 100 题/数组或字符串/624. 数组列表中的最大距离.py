# -*- coding: utf-8 -*-
# Time    : 2023/5/27 22:30
# Author  : Walter
# File    : 624. 数组列表中的最大距离.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
# 给定m个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。
# 两个整数a和b之间的距离定义为它们差的绝对值 | a - b | 。你的任务就是去找到最大距离
#
# 示例
# 1：
# 输入：
# [[1, 2, 3],
#  [4, 5],
#  [1, 2, 3]]
# 输出： 4
# 解释：
# 一种得到答案4的方法是从第一个数组或者第三个数组中选择1，同时从第二个数组中选择5 。
#
# 注意：
# 每个给定数组至少会有1个数字。列表中至少有两个非空数组。所有
# m个数组中的数字总数目在范围[2, 10000]内。
# m个数组中所有整数的范围在[-10000, 10000]内。
from typing import List


# 方法一：枚举 [超出时间限制]
class Solution:
    def maxDistance(self, list: List[List[int]]) -> int:
        res = 0
        for i in range(len(list) - 1):
            for j in range(i + 1, len(list)):
                res = max(res, abs(list[i][0] - list[j][len(list[j]) - 1]))
                res = max(res, abs(list[j][0] - list[i][len(list[i]) - 1]))
        return res


# 方法二：线性扫描
class Solution2:
    def maxDistance(self, list: List[List[int]]) -> int:
        res = 0
        min_val, max_val = list[0][0], list[0][-1]
        for i in range(1, len(list)):
            res = max(res, max(abs(list[i][-1] - min_val), abs(max_val - list[i][0])))
            min_val = min(min_val, list[i][0])
            max_val = max(max_val, list[i][-1])
        return res


print(Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
print(Solution2().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
