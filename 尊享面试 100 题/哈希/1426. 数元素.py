# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:16
# Author  : Walter
# File    : 1426. 数元素.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一个整数数组arr， 对于元素 x ，只有当 x + 1 也在数组arr 里时，才能记为 1 个数。
如果数组arr 里有重复的数，每个重复的数单独计算。

示例 1：
输入：arr = [1,2,3]
输出：2
解释：1 和 2 被计算次数因为 2 和 3 在数组 arr 里。

示例 2：
输入：arr = [1,1,3,3,5,5,7,7]
输出：0
解释：所有的数都不算, 因为数组里没有 2、4、6、8。

提示：
1 <= arr.length <= 1000
0 <= arr[i] <= 1000
'''
# Python3 字典模拟
from collections import Counter
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        dic = Counter(arr)
        res = 0
        for a in arr:
            if (a + 1) in dic:
                res += 1
        return res

# Python3 统计
class Solution2:
    def countElements(self, arr: List[int]) -> int:
        aset = set(arr)
        res = 0
        for a in arr:
            if (a+1) in aset:
                res += 1
        return res

class Solution3:
    def countElements(self, arr: List[int]) -> int:
        count=0
        for i in arr:
            if i+1 in arr:
                count += 1
        return count


print(Solution().countElements([1, 2, 3]))
print(Solution2().countElements([1, 2, 3]))
print(Solution3().countElements([1, 2, 3]))