# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 0:00
# @Author  : Walter
# @File    : 415. 字符串相加.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给定两个字符串形式的非负整数num1 和num2，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger），也不能直接将输入的字符串转换为整数形式。

示例 1：
输入：num1 = "11", num2 = "123"
输出："134"

示例 2：
输入：num1 = "456", num2 = "77"
输出："533"

示例 3：
输入：num1 = "0", num2 = "0"
输出："0"
'''


# 方法一：模拟
class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""
        while m >= 0 or n >= 0:
            n1 = int(num1[m]) if m >= 0 else 0  # 可能最高位为空需要补0
            n2 = int(num2[n]) if n >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            m -= 1
            n -= 1
        return "1" + res if carry else res


class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, ans, carry = len(num1) - 1, len(num2) - 1, '', 0
        while i >= 0 and j >= 0:
            s = carry + ord(num1[i]) + ord(num2[j]) - ord('0') * 2
            ans = str(s % 10) + ans
            carry = s // 10
            i -= 1
            j -= 1
        while i >= 0:
            s = carry + ord(num1[i]) - ord('0')
            ans = str(s % 10) + ans
            carry = s // 10
            i -= 1
        while j >= 0:
            s = carry + ord(num2[j]) - ord('0')
            ans = str(s % 10) + ans
            carry = s // 10
            j -= 1
        if carry == 1:
            ans = '1' + ans
        return ans


class Solution3:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, arr, carry = len(num1) - 1, len(num2) - 1, [], 0
        while i >= 0 and j >= 0:
            s = carry + ord(num1[i]) + ord(num2[j]) - ord('0') * 2
            arr.append(str(s % 10))
            carry = s // 10
            i -= 1
            j -= 1
        while i >= 0:
            s = carry + ord(num1[i]) - ord('0')
            arr.append(str(s % 10))
            carry = s // 10
            i -= 1
        while j >= 0:
            s = carry + ord(num2[j]) - ord('0')
            arr.append(str(s % 10))
            carry = s // 10
            j -= 1
        if carry == 1:
            arr.append('1')
        arr.reverse()
        return ''.join(arr)

class Solution4:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))

print(Solution1().addStrings('11', '123'))
print(Solution2().addStrings('11', '123'))
print(Solution3().addStrings('11', '123'))
print(Solution4().addStrings('11', '123'))