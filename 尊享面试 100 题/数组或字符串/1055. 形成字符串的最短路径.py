# -*- coding: utf-8 -*-
# Time    : 2023/5/28 11:50
# Author  : Walter
# File    : 1055. 形成字符串的最短路径.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
对于任何字符串，我们可以通过删除其中一些字符（也可能不删除）来构造该字符串的子序列 。(例如，“ace” 是 “abcde” 的子序列，而 “aec” 不是)。
给定源字符串source和目标字符串target，返回源字符串source中能通过串联形成目标字符串target的子序列的最小数量 。如果无法通过串联源字符串中的子序列来构造目标字符串，则返回 - 1。

示例1：
输入：source = "abc", target = "abcbc"
输出：2
解释：目标字符串"abcbc"可以由"abc"和"bc"形成，它们都是源字符串"abc"的子序列。

示例2：
输入：source = "abc", target = "acdbc"
输出：-1
解释：由于目标字符串中包含字符"d"，所以无法由源字符串的子序列构建目标字符串。

示例3：
输入：source = "xyz", target = "xzyxz"
输出：3
解释：目标字符串可以按如下方式构建： "xz" + "y" + "xz"。

提示：
1 <= source.length, target.length <= 1000
source和target仅包含英文小写字母。
'''

'''
初始化计数器 count 为 0。
遍历目标字符串 target 的字符，并用一个指针 source_ptr 在源字符串 source 中寻找相匹配的字符。
当找到匹配的字符时，移动 source_ptr 到下一个字符。
如果 source_ptr 到达源字符串 source 的末尾，说明我们已经找到一个子序列，那么将计数器 count 加 1，并将 source_ptr 重置为 0。
重复步骤 2-4 直到遍历完目标字符串 target。
如果计数器 count 为 0，则返回 -1，否则返回 count。
'''
class Solution:
    def shortest_way_to_form_string(self, source: str, target: str) -> int:
        count = 0
        target_ptr = 0

        while target_ptr < len(target):
            source_ptr = 0
            found_subsequence = False

            while source_ptr < len(source) and target_ptr < len(target):
                if source[source_ptr] == target[target_ptr]:
                    target_ptr += 1
                    found_subsequence = True
                source_ptr += 1

            if not found_subsequence:
                return -1
            count += 1

        return count


print(Solution().shortest_way_to_form_string("abc", "abcbc"))
