# -*- coding: utf-8 -*-
# Time    : 2023/5/30 23:25
# Author  : Walter
# File    : 1180. 统计只含单一字母的子串.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一个字符串 s，返回 只含 单一字母 的子串个数 。

示例 1：
输入： s = "aaaba"
输出： 8
解释： 只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
"aaa" 出现 1 次。
"aa" 出现 2 次。
"a" 出现 4 次。
"b" 出现 1 次。
所以答案是 1 + 2 + 4 + 1 = 8。

示例 2:
输入： s = "aaaaaaaaaa"
输出： 55

提示：
1 <= s.length <= 1000
s[i] 仅由小写英文字母组成
'''
# 方法一：分组计算
'''
解题思路：
本题要求只含单一字母的子串个数，首先我们可以计算每一个最长只含单一字母的连续子串。
比如 s = "aaabb"，一共有两个符合要求的子串，分别为 aaa 和 bb。
然后考虑对于一个字符串，共有多少不同的子串。我们可以对字符串进行分组计算，
比如 aaa 共有 6 个子串。a 3 个， aa 2 个，aaa 1 个。转化为通用公式就是 n * (n + 1) / 2，其中 n 为连续子串的长度。
遍历字符串 s， 计算每个最长只含单一字母的连续子串的长度 count，
每个最长连续子串可以分成 count * (count + 1) / 2 个不同的子串，将其累加到结果中。
'''


class Solution:
    def countLetters(self, s: str) -> int:
        ans = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                ans += count * (count + 1) // 2
                count = 1
        ans += count * (count + 1) // 2
        return ans


sol = Solution()
print(sol.countLetters("aaaba"))
