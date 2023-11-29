# -*- coding: utf-8 -*-
# Time : 2023/11/29 15:12
# Author : Walter
# File : 子数组最大平均数 I.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :

'''
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

任何误差小于 10-5 的答案都将被视为正确答案。



示例 1：

输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
示例 2：

输入：nums = [5], k = 1
输出：5.00000


提示：

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''
import math
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)

        return maxTotal / k


    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        # Step 1
        # 定义需要维护的变量
        # 本题求最大平均值 (其实就是求最大和)，所以需要定义sum_, 同时定义一个max_avg (初始值为负无穷)
        sum_, max_avg = 0, -math.inf

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(nums)):
            # Step 3: 更新需要维护的变量 (sum_), 不断把当前值积累到sum_上
            sum_ += nums[end]

            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口首指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (sum_, max_avg)
            if end >= k - 1:
                max_avg = max(max_avg, sum_ / k)
                sum_ -= nums[start]
                start += 1
        return max_avg

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(Solution().findMaxAverage(nums, k))
print(Solution().findMaxAverage2(nums, k))
