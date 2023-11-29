# -*- coding: utf-8 -*-
# Time : 2023/11/29 15:18
# Author : Walter
# File : 1763. 最长的美好子字符串.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :
'''
当一个字符串 s 包含的每一种字母的大写和小写形式 同时 出现在 s 中，就称这个字符串 s 是 美好 字符串。比方说，"abABB" 是美好字符串，因为 'A' 和 'a' 同时出现了，且 'B' 和 'b' 也同时出现了。然而，"abA" 不是美好字符串因为 'b' 出现了，而 'B' 没有出现。

给你一个字符串 s ，请你返回 s 最长的 美好子字符串 。如果有多个答案，请你返回 最早 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。



示例 1：

输入：s = "YazaAay"
输出："aAa"
解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
"aAa" 是最长的美好子字符串。
示例 2：

输入：s = "Bb"
输出："Bb"
解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。
示例 3：

输入：s = "c"
输出：""
解释：没有美好子字符串。
示例 4：

输入：s = "dDzeE"
输出："dD"
解释："dD" 和 "eE" 都是最长美好子字符串。
由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。


提示：

1 <= s.length <= 100
s 只包含大写和小写英文字母。
'''

# 方法一：枚举
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        maxPos, maxLen = 0, 0
        for i in range(n):
            lower, upper = 0, 0
            for j in range(i, n):
                if s[j].islower():
                    lower |= 1 << (ord(s[j]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[j]) - ord('A'))
                if lower == upper and j - i + 1 > maxLen:
                    maxPos = i
                    maxLen = j - i + 1
        return s[maxPos: maxPos + maxLen]

# 方法二：分治
class Solution2:
    def longestNiceSubstring2(self, s: str) -> str:
        maxPos, maxLen = 0, 0
        def dfs(start, end):
            nonlocal maxPos, maxLen
            if start >= end:
                return
            lower, upper = 0, 0
            for i in range(start, end + 1):
                if s[i].islower():
                    lower|= 1 << (ord(s[i]) - ord('a'))
                else:
                    upper|= 1 << (ord(s[i]) - ord('A'))
            if lower == upper:
                if end - start + 1 > maxLen:
                    maxPos, maxLen = start, end - start + 1
                return
            pos, valid = start, lower & upper
            while pos <= end:
                start = pos
                while pos <= end and valid & (1 << (ord(s[pos].lower()) - ord('a'))):
                    pos += 1
                dfs(start, pos - 1)
                pos += 1
        dfs(0, len(s) - 1)
        return s[maxPos : maxPos + maxLen]

# 方法三：滑动窗口
class Solution3:
    def longestNiceSubstring3(self, s: str) -> str:
        def check(typeNum):
            nonlocal maxPos, maxLen
            lowerCnt = [0] * 26
            upperCnt = [0] * 26
            l, r, total, cnt = 0, 0, 0, 0
            while r < len(s):
                idx = ord(s[r].lower()) - ord('a')
                if s[r].islower():
                    lowerCnt[idx] += 1
                    if lowerCnt[idx] == 1 and upperCnt[idx] > 0:
                        cnt += 1
                else:
                    upperCnt[idx] += 1
                    if upperCnt[idx] == 1 and lowerCnt[idx] > 0:
                        cnt += 1
                if lowerCnt[idx] + upperCnt[idx] == 1:
                    total += 1

                while total > typeNum:
                    idx = ord(s[l].lower()) - ord('a')
                    if lowerCnt[idx] + upperCnt[idx] == 1:
                        total -= 1
                    if s[l].islower():
                        lowerCnt[idx] -= 1
                        if lowerCnt[idx] == 0 and upperCnt[idx] > 0:
                            cnt -= 1
                    else:
                        upperCnt[idx] -= 1
                        if upperCnt[idx] == 0 and lowerCnt[idx] > 0:
                            cnt -= 1
                    l += 1
                if cnt == typeNum and r - l + 1 > maxLen:
                    maxPos, maxLen = l, r - l + 1
                r += 1

        maxPos, maxLen = 0, 0
        types = len(set(s.lower()))
        for i in range(1, types + 1):
            check(i)
        return s[maxPos: maxPos + maxLen]


print(Solution().longestNiceSubstring("YazaAay"))
print(Solution2().longestNiceSubstring2("YazaAay"))
print(Solution3().longestNiceSubstring3("YazaAay"))