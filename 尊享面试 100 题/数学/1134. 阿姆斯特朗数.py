# -*- coding: utf-8 -*-
# Time    : 2023/5/30 23:27
# Author  : Walter
# File    : 1134. 阿姆斯特朗数.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一个整数 n ，让你来判定他是否是 阿姆斯特朗数，是则返回 true，不是则返回 false。
假设存在一个 k 位数 n ，其每一位上的数字的 k 次幂的总和也是 n ，那么这个数是阿姆斯特朗数 。

示例 1：
输入：n = 153
输出：true
示例：
153 是一个 3 位数，且 153 = 13 + 53 + 33。

示例 2：
输入：n = 123
输出：false
解释：123 是一个 3 位数，且 123 != 13 + 23 + 33 = 36。

提示：
1 <= n <= 108
'''
'''
解题思路：
阿姆斯特朗数定义：k 位数 N，其每一位上的数字的 k 次幂的总和也是 N。
所以只需要计算数字的长度 k，再计算每一位对应的值。
根据上面的定义，首先需要求出这个数字的位数 k，有两种方法：
使用除 10 法求数字的位数，当数字大于 0 时，除以 10 并且位数加一，算法如下：
k := 0
for N > 0
    k++
    N = N/10
将数字 N 转化为字符串，直接求字符串长度。这种方法显然没有上面的方法好，但是简单明了，算法如下：
k = string(N).len()
得到位数 k 后，只需要再遍历 N 上每一个数字，计算数字的 k 次幂并累加。
同样我们可以使用除 10 法遍历数字的每一位，遍历过程中除 10 取余的结果就是当前的位数。
最后把求出的数和 N 比较是否相等。
第一步的第二种方法将 N 转化为字符串求 k。我们还可以使用此方法一步到底，
在第二步同样遍历字符串，把每一位直接转换成数字求值（python 代码给出了此解法）。
'''


class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        k = len(str(N))
        sum = 0
        for i in str(N):
            sum += int(i) ** k
        return sum == N
