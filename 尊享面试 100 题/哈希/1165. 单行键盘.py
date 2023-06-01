# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:15
# Author  : Walter
# File    : 1165. 单行键盘.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
我们定制了一款特殊的键盘，所有的键都 排列在一行上 。
给定一个长度为 26 的字符串 keyboard ，来表示键盘的布局(索引从 0 到 25 )。一开始，你的手指在索引 0 处。要输入一个字符，你必须把你的手指移动到所需字符的索引处。手指从索引 i 移动到索引 j 所需要的时间是 |i - j|。
您需要输入一个字符串 word 。写一个函数来计算用一个手指输入需要多少时间。

示例 1：
输入：keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
输出：4
解释：从 0 号键移动到 2 号键来输出 'c'，又移动到 1 号键来输出 'b'，接着移动到 0 号键来输出 'a'。
总用时 = 2 + 1 + 1 = 4.

示例 2：
输入：keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
输出：73

提示：
keyboard.length == 26
keyboard 按某种特定顺序排列，并包含每个小写英文字母一次。
1 <= word.length <= 104
word[i] 为小写英文字母
'''


# 方法一：暴力法
# 解题思路：
# 记录机械手上一个位置 pre（初始为 0）。遍历字符串 word，对于每一个字符 word[i]，再遍历 keyboard 找到对应的下标。
# 对应下标和上一个位置 pre 的差就是移动到当前字符的时间，同样的方法计算所有字符的移动时间并累加即可。
class Solution(object):
    def calculate_time(self, keyboard, word):
        sum, pre = 0, 0
        for i in range(len(word)):
            for j in range(26):
                if keyboard[j] == word[i]:
                    sum += abs(j - pre)  # 计算移动到当前字符的时间
                    pre = j  # 保存上一个位置
                    break
        return sum

    def abs(x):
        if x < 0:
            return -1 * x
        return x


# 方法二：哈希表
class Solution2(object):
    def calculate_time(self, keyboard, word):
        m = {}
        # 构建哈希表，记录每个字符的下标
        for i in range(len(keyboard)):
            m[keyboard[i]] = i
        sum, pre = 0, 0
        for i in range(len(word)):
            sum += abs(m[word[i]] - pre)
            pre = m[word[i]]
        return sum

    def abs(x):
        if x < 0:
            return -1 * x
        return x


print(Solution().calculate_time("abcdefghijklmnopqrstuvwxyz", "cba"))
print(Solution2().calculate_time("abcdefghijklmnopqrstuvwxyz", "cba"))
