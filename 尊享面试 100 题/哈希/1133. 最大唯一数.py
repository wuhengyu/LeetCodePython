# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:16
# Author  : Walter
# File    : 1133. 最大唯一数.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一个整数数组A，请找出并返回在该数组中仅出现一次的最大整数。
如果不存在这个只出现一次的整数，则返回 -1。

示例 1：
输入：[5,7,3,9,4,9,8,3,1]
输出：8
解释：
数组中最大的整数是 9，但它在数组中重复出现了。而第二大的整数是 8，它只出现了一次，所以答案是 8。

示例 2：
输入：[9,9,8,8]
输出：-1
解释：
数组中不存在仅出现一次的整数。

提示：
1 <= A.length <= 2000
0 <= A[i] <= 1000
'''
import collections
from typing import List

# 方法一：哈希表
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        m = collections.defaultdict(int)
        for num in A:
            m[num] += 1

        mx = -1
        for k, v in m.items():
            if v == 1 and k > mx:
                mx = k
        return mx

# 方法二：计数排序
class Solution2:
    def largestUniqueNumber(self, A: List[int]) -> int:
        r = [0] * 1001
        for num in A:
            r[num] += 1
        for i in range(1000, -1, -1):
            if r[i] == 1:
                return i
        return -1


print(Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
print(Solution2().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))