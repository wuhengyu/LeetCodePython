# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 0:26
# @Author  : Walter
# @File    : 461. 汉明距离.py
# @License : (C)Copyright Walter
# @Desc    :
'''
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
示例 1：
输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
示例 2：
输入：x = 3, y = 1
输出：1
'''


# 方法一：内置位计数功能
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


# 方法二：移位实现位计数
class Solution2:
    def hammingDistance2(self, x: int, y: int) -> int:
        s = x ^ y
        ret = 0
        while s != 0:
            ret += s & 1
            s >>= 1
        return ret


# 方法三：Brian Kernighan 算法
class Solution3:
    def hammingDistance3(self, x: int, y: int) -> int:
        s = x ^ y
        ret = 0
        while s != 0:
            s &= s - 1
            ret += 1
        return ret


print(Solution().hammingDistance(x=1, y=4))
print(Solution2().hammingDistance2(x=1, y=4))
print(Solution3().hammingDistance3(x=1, y=4))
