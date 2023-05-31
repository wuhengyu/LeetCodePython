# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:15
# Author  : Walter
# File    : 266. 回文排列.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。
“回文串”是一个正读和反读都一样的字符串，初始化标志flag=true，比如“level”或者“noon”等等就是回文串。
示例 1：
输入: "code"
输出: false

示例 2：
输入: "aab"
输出: true

示例 3：
输入: "carerac"
输出: true
'''
# 方法一：穷举
'''
解题思路：如果一个字符串可以组成一个回文串，那么：
(1) 如果它的长度为偶数，那么每个字符都必须出现偶数次；
(2) 如果它的长度为奇数，那么除了一个字符出现奇数次以外，其它的字符都必须出现偶数次。
因此可以总结得到，如果一个字符串可以组成一个回文串，那么出现奇数次的字符的数量不能超过 1。
由于字符串中出现的字符的 ASCII 码在 0 到 127 之间，因此我们可以枚举所有的字符，对于每一个字符 
c，我们找出它在字符串中出现的次数 ct，如果 ct 为奇数，那么我们将计数器count 的值增加 1。如果在某一个时刻 
count 的值大于 1，那么说明至少有两个字符出现了奇数次，因此字符串就不能组成一个回文串。如果在枚举完成后，count 的值仍然小于等于 1，那么字符串就可以组成一个回文串。
'''
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        for i in range(97, 128):
            ct = 0
            for j in range(len(s)):
                if ord(s[j]) == i:
                    ct += 1
            count += ct % 2
            if count > 1:
                return False
        return True
# 方法二：基于哈希的映射表（HashMap）
class Solution2:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        count = 0
        for key in freq:
            count += freq[key] % 2
        return count <= 1
# 方法三：数组
class Solution3:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = [0] * 128
        for c in s:
            freq[ord(c)] += 1
        count = 0
        for key in range(128):
            count += freq[key] % 2
            if count > 1:
                return False
        return True
# 方法四：数组+单次循环
class Solution4:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = [0] * 128
        count = 0
        for c in s:
            freq[ord(c)] += 1
            if freq[ord(c)] % 2 == 0:
                count -= 1
            else:
                count += 1
        return count <= 1
# 方法五：集合
class Solution5:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = set()
        for c in s:
            if c in seen:
                seen.remove(c)
            else:
                seen.add(c)
        return len(seen) <= 1


print(Solution().canPermutePalindrome('aab'))
print(Solution2().canPermutePalindrome('aba'))
print(Solution3().canPermutePalindrome('aab'))
print(Solution4().canPermutePalindrome('abcdcd'))
print(Solution5().canPermutePalindrome('abcdabcd'))
