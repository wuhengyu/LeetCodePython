# -*- coding: utf-8 -*-
# @Time    : 2022/12/23 0:29
# @Author  : Walter
# @File    : 283. 移动零.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意，必须在不复制数组的情况下原地对数组进行操作。
示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:
输入: nums = [0]
输出: [0]
提示:
1 <= nums.length <= 104
-231<= nums[i] <= 231- 1
进阶：你能尽量减少完成的操作次数吗？
'''
from typing import List


# 方法一：双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> list[int]:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums
listnums = [0,1,0,3,12]
print(Solution().moveZeroes(listnums))