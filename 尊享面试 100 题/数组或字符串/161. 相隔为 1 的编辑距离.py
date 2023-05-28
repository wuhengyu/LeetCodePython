# -*- coding: utf-8 -*-
# Time    : 2023/5/28 11:26
# Author  : Walter
# File    : 161. 相隔为 1 的编辑距离.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给定两个字符串 s 和 t ，如果它们的编辑距离为 1 ，则返回 true ，否则返回 false 。
字符串 s 和字符串 t 之间满足编辑距离等于 1 有三种可能的情形：
往 s 中插入 恰好一个 字符得到 t
从 s 中删除 恰好一个 字符得到 t
在 s 中用 一个不同的字符 替换 恰好一个 字符得到 t

示例 1：
输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。

示例 2:
输入: s = "cab", t = "ad"
输出: false
解释: 无法通过 1 步操作使 s 变为 t。

提示:
0 <= s.length, t.length <= 104
s 和 t 由小写字母，大写字母和数字组成
'''
# 方法一：分情况讨论

'''
假设字符串 sss 和 ttt 的长度分别是 mmm 和 nnn。
如果 sss 和 ttt 的编辑距离为 111，则可能有三种情况：
往 sss 中插入一个字符得到 ttt，此时 n−m=1n - m = 1n−m=1，ttt 比 sss 多一个字符，其余字符都相同；
从 sss 中删除一个字符得到 ttt，此时 m−n=1m - n = 1m−n=1，sss 比 ttt 多一个字符，其余字符都相同；
将 sss 中的一个字符替换成不同的字符得到 ttt，此时 m=nm = nm=n，sss 和 ttt 恰好有一个字符不同。
根据上述分析，当 sss 和 ttt 的编辑距离为 111 时，sss 和 ttt 的长度关系可能有三种情况，分别是 n−m=1n - m = 1n−m=1、m−n=1m - n = 1m−n=1 和 m=nm = nm=n。首先计算 sss 和 ttt 的长度关系，在可能的三种情况中找到对应的一种情况，然后遍历字符串判断编辑距离是否为 111。
如果长度关系不符合上述三种情况，即 ∣m−n∣>1|m - n| > 1∣m−n∣>1，则编辑距离不为 111。
具体实现方法如下。
当 n−m=1n - m = 1n−m=1 或 m−n=1m - n = 1m−n=1 时，由于两种情况具有对称性，因此可以定义一个函数统一计算这两种情况。用 longer\textit{longer}longer 表示较长的字符串，shorter\textit{shorter}shorter 表示较短的字符串，同时遍历两个字符串，
比较对应下标处的字符是否相同，如果字符相同则将两个字符串的下标同时加 111，如果字符不同则只将 longer\textit{longer}longer 的下标加 111。遍历过程中如果出现两个字符串的下标之差大于 111 则不符合一次编辑，遍历结束时如果两个字符串的下标之差不大于 111 则符合一次编辑。
当 m=nm = nm=n 时，同时遍历 sss 和 ttt，比较相同下标处的字符是否相同。如果字符不同的下标个数等于 111，则编辑距离为 111。
'''


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m < n:
            return self.isOneEditDistance(t, s)
        if m - n > 1:
            return False
        foundDifference = False
        for i, (x, y) in enumerate(zip(s, t)):
            if x != y:
                foundDifference = True
                return s[i + 1:] == t[i + 1:] if m == n else s[i + 1:] == t[i:]  # 注：改用下标枚举可达到 O(1) 空间复杂度
        return foundDifference or m - n == 1


print(Solution().isOneEditDistance("ab", "acb"))
print(Solution().isOneEditDistance("ab", "acbd"))
