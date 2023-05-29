# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:14
# Author  : Walter
# File    : 159. 至多包含两个不同字符的最长子串.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一个字符串 s ，请你找出至多包含 两个不同字符 的最长子串，并返回该子串的长度。

示例 1：
输入：s = "eceba"
输出：3
解释：满足题目要求的子串是 "ece" ，长度为 3 。

示例 2：
输入：s = "ccaabbb"
输出：5
解释：满足题目要求的子串是 "aabbb" ，长度为 5 。

提示：
1 <= s.length <= 105
s 由英文字母组成
'''
# 方法 1：滑动窗口
# 解题思路：一开始，让两个指针都指向 0 ，当窗口包含的字符不超过 2 个不同的字符时，就不断将右指针往右边移动。如果在某一个位置有 3 个不同的字符，就开始移动左指针，直到窗口内包含不超过 2 个不同字符。

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        left, right = 0, 0
        hashmap = defaultdict()
        max_len = 2

        while right < n:
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1

            if len(hashmap) == 3:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right - left)
        return max_len


print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))