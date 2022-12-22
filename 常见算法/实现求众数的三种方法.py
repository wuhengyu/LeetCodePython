# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 20:31
# @Author  : Walter
# @File    : 实现求众数的三种方法.py
# @License : (C)Copyright Walter
# @Desc    :

# 方案1：字典（哈希表）
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:                                                # 统计每个数字出现的次数
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return {v: k for k, v in count.items()}[max(count.values())]    # 字典键值反转，找到出现次数最多的数字

# 方案2：数字统计
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, res = 0, nums[0]         # 初始化计数器和结果
        for i in range(len(nums)-1):    # 遍历数组中每一个数
            if nums[i] == res:          # 如果当前的数和结果变量相同
                count += 1              # 计数器+1
            else:                       # 否则
                count -= 1              # 计数器-1
                if count == 0:          # 如果减到了0
                    res = nums[i+1]     # 那么更新结果变量为下一个数
        return res                      # 返回结果


# 方案3：排序
class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        return nums[len(nums) // 2]



nums = [1, 2, 3, 4, 5, 2, 2, 3, 2, 4, 5, 6]
print(Solution().majorityElement(nums))
print(Solution2().majorityElement(nums))
print(Solution3().majorityElement(nums))