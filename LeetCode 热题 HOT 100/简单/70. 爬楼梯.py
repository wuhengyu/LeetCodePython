# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 21:07
# @Author  : Walter
# @File    : 70. 爬楼梯.py
# @License : (C)Copyright Walter
# @Desc    :
'''
假设你正在爬楼梯。需要 n阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
'''


# 方法一：动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 0, 1
        for i in range(1, n + 1):
            p, q, r = q, r, p + q
        return r


# 方法二：矩阵快速幂
class Solution2:
    def climbStairs2(self, n: int) -> int:
        q = [[1, 1], [1, 0]]
        res = self.pow(q, n)
        return res[0][0]

    def pow(self, a, n):
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1 == 1:
                ret = self.multiply(ret, a)
            n >>= 1
            a = self.multiply(a, a)
        return ret

    def multiply(self, a, b):
        c = [[0, 0] for _ in range(2)]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c


# 方法三：通项公式
import math


class Solution3:
    def climbStairs3(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return round(fibn / sqrt5)
