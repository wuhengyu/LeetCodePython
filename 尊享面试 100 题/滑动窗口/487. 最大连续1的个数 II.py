# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:14
# Author  : Walter
# File    : 487. 最大连续1的个数 II.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

'''
给定一个二进制数组 nums ，如果最多可以翻转一个 0 ，则返回数组中连续 1 的最大个数。
示例 1：
输入：nums = [1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
当翻转以后，最大连续 1 的个数为 4。

示例 2:
输入：nums = [1,0,1,1,0,1]
输出：4

提示:
1 <= nums.length <= 105
nums[i]不是0就是1.
'''
from typing import List


# 方法一：预处理 + 枚举
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        pre = [0] * n
        suff = [0] * n

        for i in range(n):
            if i:
                pre[i] = pre[i - 1]
            if nums[i]:
                pre[i] += 1
            else:
                pre[i] = 0
            ans = max(ans, pre[i])

        for i in range(n - 1, -1, -1):
            if i < n - 1:
                suff[i] = suff[i + 1]
            if nums[i]:
                suff[i] += 1
            else:
                suff[i] = 0

        for i in range(n):
            if not nums[i]:
                res = 0
                if i > 0:
                    res += pre[i - 1]
                if i < n - 1:
                    res += suff[i + 1]
                ans = max(ans, res + 1)

        return ans
# 方法二：动态规划
class Solution2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        pre = [0] * n
        suff = [0] * n

        for i in range(n):
            if i:
                pre[i] = pre[i - 1]
            if nums[i]:
                pre[i] += 1
            else:
                pre[i] = 0
            ans = max(ans, pre[i])

        for i in range(n - 1, -1, -1):
            if i < n - 1:
                suff[i] = suff[i + 1]
            if nums[i]:
                suff[i] += 1
            else:
                suff[i] = 0

        for i in range(n):
            if not nums[i]:
                res = 0
                if i > 0:
                    res += pre[i - 1]
                if i < n - 1:
                    res += suff[i + 1]
                ans = max(ans, res + 1)

        return ans


print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
print(Solution2().findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
