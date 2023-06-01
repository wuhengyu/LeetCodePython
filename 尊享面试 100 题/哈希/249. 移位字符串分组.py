# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:16
# Author  : Walter
# File    : 249. 移位字符串分组.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给定一个字符串，对该字符串可以进行 “移位” 的操作，也就是将字符串中每个字母都变为其在字母表中后续的字母，
比如："abc" -> "bcd"。这样，我们可以持续进行 “移位” 操作，从而生成如下移位序列：
"abc" -> "bcd" -> ... -> "xyz"
给定一个包含仅小写字母字符串的列表，将该列表中所有满足 “移位” 操作规律的组合进行分组并返回。
示例：
输入：["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
输出：
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
解释：可以认为字母表首尾相接，所以 'z' 的后续为 'a'，所以 ["az","ba"] 也满足 “移位” 操作规律。
'''
from collections import defaultdict
from typing import List


# 方法一：哈希+字母转数字
# 解题思路:
# 因为移动一位，所以一个单词字母之间的差和之前的保持一样，可以计算后归入同一个字典的key中
# 1.定义函数word_to_number(self, word)将字母转换为数字字符串，注意模26保证循环
# 2.遍历列表strings,对每一个单词，将其转化为数字字符串并加入相应的key对应的列表中
# 3.遍历结束后，将字典存储的值列表化并返回结果
class Solution:
    def word_to_number(self, word):
        res = ''
        if len(word) == 1:
            return ''
        for i in range(len(word) - 1):
            num = (ord(word[i + 1]) - ord(word[i])) % 26
            res += ',' + str(num)
        return res

    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        group_dict = defaultdict(list)
        for word in strings:
            group_dict[self.word_to_number(word)].append(word)
        return list(group_dict.values())


# 方法二：哈希+集合
# 解题思路：
# 建立一个单个字母移向下一个字母的字典，在此基础上，建立一个单词移向下一个单词的方法。
# 对于一个列表中的单词，不断调用此方法，检测下一个是否存在于列表中。使用字典或集合优化查询是否存在的时间复杂度。
# get_alpha_map(cls) 返回单个字母映射至下一个字母的字典
# move_string_to_next(self, words) 在1的基础上返回一个单词映射后的下一个单词
# groupStrings(self, strings: list[str]) 将列表set集合化，方便检索是否存在某个词。
# 并用Counter统计每个词的频次，为可能存在重复的单词做准备。遍历单词重复调用move_string_to_next，
# 如果下一个单词存在于字典中，则将其从字典中删除，并加入到一个单词列表中。
import string
from collections import Counter


class Solution2:
    def __init__(self):
        self.alpha_map = self.get_alpha_map()

    @classmethod
    def get_alpha_map(cls):
        """
        返回单个字母映射至下一个字母的字典
        :return:
        """
        alphas = string.ascii_lowercase
        return {alphas[i]: alphas[(i + 1) % 26] for i in range(26)}

    def move_string_to_next(self, words):
        """
        在get_alpha_map的基础上返回一个单词映射后的下一个单词
        :param words:
        :return:
        """
        if not words:
            return ''
        res = ''
        for ch in words:
            res += self.alpha_map[ch]
        return res

    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        """
        将列表set集合化，方便检索是否存在某个词。并用Counter统计每个词的频率
        为可能存在重复的单词做准备。遍历单词重复调用move_string_to_next
        如果下一个单词存在于字典中，则将其从字典中删除，并加入到一个单词列表中。
        :param strings:
        :return:
        """
        string_set = set(strings)
        counts = Counter(strings)
        res = list()
        while string_set:
            # 随机从集合中返回一个词，并以此词为入口开始遍历
            tmp_word = string_set.pop()
            tmp = [tmp_word] * counts[tmp_word]
            # 26次必然达成一个循环
            for _ in range(26):
                tmp_word = self.move_string_to_next(tmp_word)
                if tmp_word in string_set:
                    # 如果下一个词存在，则将其频次个数的词加入列表中
                    tmp.extend([tmp_word] * counts[tmp_word])
                    string_set.remove(tmp_word)
            # 每一轮遍历结束后，加入整体返回的列表中
            res.append(tmp)
        return res


# 方法三：只用hash表，巧妙计算key值
class Solution3:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strings:
            if s[0] == 'a':
                mp[s].append(s)
            else:
                key = list(s)
                for i in range(len(s)):
                    key[i] = chr((ord(key[i]) - ord(s[0]) + 26) % 26 + ord('a'))
                key = ''.join(key)
                mp[key].append(s)

        res = []
        for mode, sublist in mp.items():
            res.append(sublist)

        return res


print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
print(Solution2().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
print(Solution3().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
