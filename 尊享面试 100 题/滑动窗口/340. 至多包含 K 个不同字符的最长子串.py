# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:14
# Author  : Walter
# File    : 340. 至多包含 K 个不同字符的最长子串.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

'''
给你一个字符串 s 和一个整数 k ，请你找出至多包含 k 个 不同 字符的最长子串，并返回该子串的长度。

示例 1：
输入：s = "eceba", k = 2
输出：3
解释：满足题目要求的子串是 "ece" ，长度为 3 。

示例 2：
输入：s = "aa", k = 1
输出：2
解释：满足题目要求的子串是 "aa" ，长度为 2 。

提示：
1 <= s.length <= 5 * 104
0 <= k <= 50
'''
# 方法 1：滑动窗口 + 哈希表
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: 'str', k: 'int') -> 'int':
        n = len(s)
        if k == 0 or n == 0:
            return 0

        left, right = 0, 0
        hashmap = defaultdict()
        max_len = 1
        while right < n:
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) == k + 1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right - left)
        return max_len

# 方法 2：滑动窗口 + 有序字典
from collections import OrderedDict


class Solution2:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0 or n == 0:
            return 0
        left, right = 0, 0
        hashmap = OrderedDict()
        max_len = 1
        while right < n:
            character = s[right]
            if character in hashmap:
                del hashmap[character]
            hashmap[character] = right
            right += 1
            if len(hashmap) == k + 1:
                _, del_idx = hashmap.popitem(last=False)
                left = del_idx + 1
            max_len = max(max_len, right - left)
        return max_len


print(Solution().lengthOfLongestSubstringKDistinct("eceba", 2))
print(Solution2().lengthOfLongestSubstringKDistinct("eceba", 2))