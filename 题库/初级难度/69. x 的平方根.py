# -*- coding: utf-8 -*-
# @Time    : 2022/11/14 15:03
# @Author  : Walter
# @File    : 69. x 的平方根.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你一个非负整数 x ，计算并返回x的 算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

示例 1：

输入：x = 4
输出：2
示例 2：

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
'''
import math

# 方法一：袖珍计算器算法
class Solution1:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


# 方法二：二分查找
class Solution2:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

# 方法三：牛顿迭代
class Solution3:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


print(Solution1().mySqrt(16))
print(Solution2().mySqrt(4))
print(Solution3().mySqrt(18))

# 返回 x 的自然对数（底为 e ）, 底数，默认为 e
print(math.log(2))
print(math.log(2, 10))
# e的x 次幂
print(math.exp(3))