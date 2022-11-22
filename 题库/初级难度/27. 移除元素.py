# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 20:06
# @Author  : Walter
# @File    : 27. 移除元素.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素

示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
'''
from typing import List


# 方法一：双指针
class Solution1:
    def removeElement(self, nums: List[int], val) -> int:
        fl = sl = 0
        a = len(nums)
        while fl < a:
            if nums[fl] != val:
                nums[sl] = nums[fl]
                sl += 1
            fl += 1
        return sl


# 方法二：双指针优化
class Solution2:
    def removeElement(self, nums2: List[int], val) -> int:
        left = 0
        right = len(nums2)
        while left < right:
            if nums2[left] == val:
                nums2[left] = nums2[right - 1]
                right -= 1
            left += 1
        return left


nums1 = [3, 2, 2, 3]
val1 = 3
print(Solution1().removeElement(nums1, val1))

nums2 = [3, 2, 2, 3]
val2 = 3
print(Solution2().removeElement(nums2, val2))
