# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 0:37
# @Author  : Walter
# @File    : 1. 两数之和 .py
# @License : (C)Copyright Walter
# @Desc    :
'''
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
'''
from typing import List


# nums = [2,7,11,15]
# target = 9
# 方法一：暴力枚举
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 方法二：哈希表
class Solution2:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 创建哈希表
        hashtable = dict()
        for i, num in enumerate(nums):
            # 判断是否存在于哈希表
            if target - num in hashtable:
                # 如何遍历之差target - num存在哈希表，返回之差hashtable[target - num]的下标，和当前下标i
                return [hashtable[target - num], i]
            # 如果不在，就把数组的值和索引存于哈希表
            hashtable[nums[i]] = i
        return []


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
print(Solution2().twoSum2(nums, target))
