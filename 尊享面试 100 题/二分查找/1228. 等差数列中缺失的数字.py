# -*- coding: utf-8 -*-
# Time : 2023/5/29 18:52
# Author : Walter
# File : 1228. 等差数列中缺失的数字.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :
'''
在某个数组arr中，值符合等差数列的数值规律：在0 <= i < arr.length - 1的前提下，arr[i+1] - arr[i]的值都相等。
我们会从该数组中删除一个 既不是第一个 也不是最后一个的值，得到一个新的数组arr。
给你这个缺值的数组arr，返回 被删除的那个数 。

示例 1：
输入：arr = [5,7,11,13]
输出：9
解释：原来的数组是 [5,7,9,11,13]。

示例 2：
输入：arr = [15,13,12]
输出：14
解释：原来的数组是 [15,14,13,12]。

提示：
3 <= arr.length <= 1000
0 <= arr[i] <= 105
给定的数组 保证 是一个有效的数组。
'''
from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return arr[0] if arr[-1] - arr[0] == 0 else list(set(range(arr[0],arr[-1], (arr[-1] - arr[0]) // len(arr))) - set(arr))[0]


class Solution2:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        a1 = arr[0]
        an = arr[-1]
        n = len(arr)
        sn = (a1 + an) * (n + 1) // 2
        for i in arr:
            sn -= i
        return sn
# 方法一：根据缺失元素的前一个元素或后一个元素求解

# 方法二：根据等差数列求和公式求解

print(Solution().missingNumber([5, 7, 11, 13]))
print(Solution2().missingNumber([5, 7, 11, 13]))