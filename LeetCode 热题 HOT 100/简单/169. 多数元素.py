# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 17:28
# @Author  : Walter
# @File    : 169. 多数元素.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给定个大小为 n 的数组nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例1：
输入：nums = [3,2,3]
输出：3
示例2：
输入：nums = [2,2,1,1,1,2,2]
输出：2
提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
'''
import collections
import random
from typing import List


# 方法一：哈希表
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# 方法二：排序
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(len(nums) // 2)]

# 方法三：随机化
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


nums = [1, 2, 3, 4, 5, 2, 2, 3, 2, 4, 5, 6]
# print(Solution().majorityElement(nums))
# print(Solution2().majorityElement(nums))
# print(Solution3().majorityElement(nums))


count = {1: 1, 2: 4, 3: 2, 4: 2, 5: 2, 6: 1}
print({v: k for k, v in count.items()})
print({v: k for k, v in count.items()}[max(count.values())])