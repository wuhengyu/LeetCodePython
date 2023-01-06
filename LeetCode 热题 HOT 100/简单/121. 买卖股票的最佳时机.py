# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 21:00
# @Author  : Walter
# @File    : 121. 买卖股票的最佳时机.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给定一个数组 prices ，它的第i个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
from typing import List


# 方法一：暴力法
# 此方法会超时
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                ans = max(ans, prices[j] - prices[i])
        return ans


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
prices2 = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices2))


# 方法二：一次遍历
class Solution2:
    def maxProfit2(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


prices3 = [7, 1, 5, 3, 6, 4]
print(Solution2().maxProfit2(prices3))
prices4 = [7, 6, 4, 3, 1]
print(Solution2().maxProfit2(prices4))
