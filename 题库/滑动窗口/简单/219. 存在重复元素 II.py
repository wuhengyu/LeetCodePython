# -*- coding: utf-8 -*-
# Time : 2023/7/4 18:01
# Author : Walter
# File : 219. 存在重复元素 II.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :
'''
给你一个整数数组nums 和一个整数k ，判断数组中是否存在两个 不同的索引i和j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

示例1：
输入：nums = [1,2,3,1], k = 3
输出：true

示例 2：
输入：nums = [1,0,1,1], k = 1
输出：true

示例 3：
输入：nums = [1,2,3,1,2,3], k = 2
输出：false

提示：
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''
from typing import List


# 方法一：哈希表
# 通过遍历列表并使用字典来实现对元素出现位置的记录和查找，从而判断是否存在符合条件的元素对。
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))


# 方法二：滑动窗口
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False


print(Solution2().containsNearbyDuplicate([1, 2, 3, 1], 3))
print(Solution2().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))