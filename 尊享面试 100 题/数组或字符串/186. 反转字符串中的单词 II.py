# -*- coding: utf-8 -*-
# Time    : 2023/5/28 11:31
# Author  : Walter
# File    : 186. 反转字符串中的单词 II.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一个字符数组 s ，反转其中 单词 的顺序。
单词 的定义为：单词是一个由非空格字符组成的序列。s 中的单词将会由单个空格分隔。
必须设计并实现 原地 解法来解决此问题，即不分配额外的空间。

示例 1：
输入：s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出：["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

示例 2：
输入：s = ["a"]
输出：["a"]

提示：
1 <= s.length <= 105
s[i] 可以是一个英文字母（大写或小写）、数字、或是空格 ' ' 。
s 中至少存在一个单词
s 不含前导或尾随空格
题目数据保证：s 中的每个单词都由单个空格分隔
'''

'''
题意要求空间复杂度O(1)，因此必须要在原数组上直接修改；
设倒序操作为T，str = a b c，则有：
c b a = ( aT bT cT )T
因此，我们只需要将a,b,c分别倒置，再将整个str倒置，即可得到c b a。
'''


class Solution:
    def reverseWords(self, s: [str]) -> str:
        i = 0
        for j in range(len(s)):  # aT bT c
            if s[j] != ' ': continue
            self.reverse(s, i, j)
            i = j + 1
        self.reverse(s, i, len(s))  # aT bT cT
        self.reverse(s, 0, len(s))  # c b a
        return s

    def reverse(self, s, i, j):
        for k in range(i, (i + j) // 2):
            g = j - 1 - k + i
            s[k], s[g] = s[g], s[k]


print(Solution().reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]))
