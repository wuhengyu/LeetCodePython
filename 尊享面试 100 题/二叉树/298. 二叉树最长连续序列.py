# -*- coding: utf-8 -*-
# Time    : 2023/5/30 22:57
# Author  : Walter
# File    : 298. 二叉树最长连续序列.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
'''
给你一棵指定的二叉树的根节点root ，请你计算其中最长连续序列路径的长度。
最长连续序列路径是依次递增1的路径。该路径，可以是从某个初始节点到树中任意节点，
通过「父 - 子」关系连接而产生的任意路径。且必须从父节点到子节点，反过来是不可以的。

示例1：
1->3->4->5
   ↓
   2
输入：root = [1, null, 3, 2, 4, null, null, null, 5]
输出：3
解释：当中，最长连续序列是3 - 4 - 5 ，所以返回结果为3 。

示例2：
2->3->2->1
输入：root = [2, null, 3, 2, null, 1]
输出：2
解释：当中，最长连续序列是2 - 3 。注意，不是3 - 2 - 1，所以返回2 。

提示：
树中节点的数目在范围[1, 3 * 104]内
-3 * 104 <= Node.val <= 3 * 104
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法 1：自顶向下深度优先搜索
class Solution:
    def __init__(self):
        self.maxLength = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.dfs(root, None, 0)
        return self.maxLength

    def dfs(self, p: TreeNode, parent: TreeNode, length: int) -> None:
        if not p:
            return
        length = length + 1 if parent and p.val == parent.val + 1 else 1
        self.maxLength = max(self.maxLength, length)
        self.dfs(p.left, p, length)
        self.dfs(p.right, p, length)


# 不把 maxLength 作为全局变量
class Solution2:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self.dfs(root, None, 0)

    def dfs(self, p: TreeNode, parent: TreeNode, length: int) -> int:
        if not p:
            return length
        length = length + 1 if parent and p.val == parent.val + 1 else 1
        return max(length, max(self.dfs(p.left, p, length),
                               self.dfs(p.right, p, length)))


# 方法 2：自底向上深度优先搜索
class Solution3:
    def __init__(self):
        self.maxLength = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.maxLength

    def dfs(self, p: TreeNode) -> int:
        if not p:
            return 0
        L = self.dfs(p.left) + 1
        R = self.dfs(p.right) + 1
        if p.left and p.val + 1 != p.left.val:
            L = 1
        if p.right and p.val + 1 != p.right.val:
            R = 1
        length = max(L, R)
        self.maxLength = max(self.maxLength, length)
        return length


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

sol = Solution()
print(sol.longestConsecutive(root))

sol2 = Solution2()
print(sol2.longestConsecutive(root))

sol3 = Solution3()
print(sol3.longestConsecutive(root))
