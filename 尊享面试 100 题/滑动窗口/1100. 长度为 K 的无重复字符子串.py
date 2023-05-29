# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:14
# Author  : Walter
# File    : 1100. 长度为 K 的无重复字符子串.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一个字符串S，找出所有长度为K且不含重复字符的子串，请你返回全部满足要求的子串的数目。

示例 1：
输入：S = "havefunonleetcode", K = 5
输出：6
解释：
这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。

示例 2：
输入：S = "home", K = 5
输出：0
解释：
注意：K 可能会大于 S 的长度。在这种情况下，就无法找到任何长度为 K 的子串。

提示：
1 <= S.length <= 10^4
S 中的所有字符均为小写英文字母
1 <= K <= 10^4
'''

# 解题思路：这里的思路是先判断字符串的长度是否小于 K，如果是则直接返回 0。否则，对于每个长度为 K 的子串，使用 set 求出其不重复的字符个数，如果等于 K，则说明这是一个符合要求的子串，计数器加一。最终返回计数器的值即可。
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0

        ans = 0
        for i in range(len(S) - K + 1):
            sub = S[i:i + K]
            if len(set(sub)) == K:
                ans += 1

        return ans

class Solution2:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(set(s)) < k:
            return 0
        n = len(s)
        ch_idx = {}
        count = 0
        for i in range(n):
            if i < k - 1:
                ch_idx[s[i]] = i
                continue
            ch_idx[s[i]] = i
            if len(ch_idx) == k:
                count += 1
            if s[i - k + 1] in ch_idx and ch_idx[s[i - k + 1]] == i - k + 1:
                ch_idx.pop(s[i - k + 1])
        return count


class Solution3:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0
        left, right = 0, 0
        count = 0
        freq = {}
        while right < len(S):
            freq[S[right]] = freq.get(S[right], 0) + 1
            while freq[S[right]] > 1:
                freq[S[left]] -= 1
                if freq[S[left]] == 0:
                    del freq[S[left]]
                left += 1
            if right - left + 1 == K:
                count += 1
            right += 1
        return count

print(Solution().numKLenSubstrNoRepeats("havefunonleetcode", 5))
print(Solution2().numKLenSubstrNoRepeats("havefunonleetcode", 5))
print(Solution3().numKLenSubstrNoRepeats("havefunonleetcode", 5))