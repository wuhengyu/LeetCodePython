# -*- coding: utf-8 -*-
# Time    : 2023/5/28 12:16
# Author  : Walter
# File    : 1198. 找出所有行中最小公共元素.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一个 m x n 的矩阵 mat，其中每一行的元素均符合 严格递增 。请返回 所有行中的 最小公共元素 。
如果矩阵中没有这样的公共元素，就请返回 -1。

示例 1：
输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
输出：5

示例 2:
输入：mat = [[1,2,3],[2,3,4],[2,3,5]]
输出： 2

提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 104
mat[i] 已按严格递增顺序排列。
'''
from typing import List


# 方法一：统计元素出现次数
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        count = [0] * 10001
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                count[mat[i][j]] += 1
        for k in range(1, 10001):
            if count[k] == n:
                return k
        return -1


# 方法二：二分搜索
import bisect


class Solution2:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        for j in range(m):
            found = True
            for i in range(1, n):
                if bisect.bisect_left(mat[i], mat[0][j]) == len(mat[i]) or mat[i][
                    bisect.bisect_left(mat[i], mat[0][j])] != mat[0][j]:
                    found = False
                    break
            if found:
                return mat[0][j]
        return -1


# 方法三：行位置
import bisect


class Solution3:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pos, cur_max, cnt = [0] * n, 0, 0
        while True:
            for i in range(n):
                pos[i] = bisect.bisect_left(mat[i], cur_max, pos[i], m)
                if pos[i] == m:
                    return -1
                if mat[i][pos[i]] > cur_max:
                    cur_max = mat[i][pos[i]]
                    cnt = 1
                elif mat[i][pos[i]] == cur_max:
                    cnt += 1
                else:
                    break
                if cnt == n:
                    return cur_max
        return -1


print(Solution().smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
print(Solution2().smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
print(Solution3().smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
