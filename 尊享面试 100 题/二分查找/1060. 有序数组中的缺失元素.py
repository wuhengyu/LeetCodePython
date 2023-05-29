# -*- coding: utf-8 -*-
# Time    : 2023/5/29 21:47
# Author  : Walter
# File    : 1060. 有序数组中的缺失元素.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
现有一个按 升序 排列的整数数组 nums ，其中每个数字都 互不相同 。
给你一个整数 k ，请你找出并返回从数组最左边开始的第 k 个缺失数字。

示例 1：
输入：nums = [4,7,9,10], k = 1
输出：5
解释：第一个缺失数字为 5 。

示例 2：
输入：nums = [4,7,9,10], k = 3
输出：8
解释：缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8 。

示例 3：
输入：nums = [1,2,4], k = 3
输出：6
解释：缺失数字有 [3,5,6,7,...]，因此第三个缺失数字为 6 。

提示：
1 <= nums.length <= 5 * 104
1 <= nums[i] <= 107
nums 按 升序 排列，其中所有元素 互不相同 。
1 <= k <= 108
'''
from typing import List


# 方法一：线性扫描
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda idx: nums[idx] - nums[0] - idx

        n = len(nums)
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)
        idx = 1
        while missing(idx) < k:
            idx += 1
        return nums[idx - 1] + k - missing(idx - 1)


# 方法二：二分查找
class Solution2:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)
        left, right = 0, n - 1
        while left != right:
            pivot = left + (right - left) // 2
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot
        return nums[left - 1] + k - missing(left - 1)


class Solution3:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # 计算到 nums[i] 为止缺失的数字个数
        def missing(idx):
            return nums[idx] - nums[0] - idx

        # 二分查找
        while left < right:
            mid = (left + right) // 2
            if missing(mid) < k:
                # 缺失数字在右半部分
                left = mid + 1
            else:
                # 缺失数字在左半部分
                right = mid

        # 最终结果为 nums[left-1]+k-missing(left-1)，其中 left-1 为最后一个满足 missing(mid) < k 的位置
        return nums[left - 1] + k - missing(left - 1)


print(Solution().missingElement([4, 7, 9, 10], 3))
print(Solution2().missingElement([4, 7, 9, 10], 3))
print(Solution3().missingElement([4, 7, 9, 10], 3))
