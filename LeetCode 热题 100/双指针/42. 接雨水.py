# -*- coding: utf-8 -*-
# Time    : 2024/11/2 18:44
# Author  : Walter
# File    : 42. 接雨水.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

在某个位置能够盛水的上限,取决于该位置左边和右边最高柱子中较矮的那个
如果只使用一个指针从左向右扫描,对于每个位置,都需要查看它左边和右边所有的柱子高度,才能确定该位置能存多少水。这样的时间复杂度是 O(n^2),效率很低。
对于最左边和最右边的柱子,它们肯定是不能存水的。利用两个指针,可以很容易确定边界条件。
'''
from typing import List


# 方法一：动态规划
class Solution1:
    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans


# 方法二：单调栈
class Solution2:
    def trap2(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans


# 方法三：双指针
class Solution3:
    def trap3(self, height: List[int]) -> int:
        # ans是用来存储最终的结果, 初始值为0
        ans = 0
        # left和right分别是左右两个指针, 初始时分别指向height列表的第一个和最后一个元素。
        left, right = 0, len(height) - 1
        # leftMax和rightMax分别记录了从左边和右边看过去, 当前最高的柱子高度
        leftMax = rightMax = 0
        # 直到左右两个指针相遇为止
        while left < right:
            # 更新leftMax和rightMax, 保持它们分别是从左边和右边看过去的最高柱子高度
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                # 左边柱子能盛水的量, 取决于它和从左边数过来的最高柱子(leftMax)之间的高度差
                ans += leftMax - height[left]
                left += 1
            else:
                # 右边柱子能盛水的量, 取决于它和从右边数过来的最高柱子(rightMax)之间的高度差
                ans += rightMax - height[right]
                right -= 1

        return ans


print(Solution1().trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution2().trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution3().trap3([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
