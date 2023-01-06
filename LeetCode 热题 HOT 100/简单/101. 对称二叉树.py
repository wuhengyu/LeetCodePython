# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 21:25
# @Author  : Walter
# @File    : 101. 对称二叉树.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。
     1
  2      2
3  4   4  3
输入：root = [1,2,2,3,4,4,3]
输出：true
     1
  2      2
     3      3
输入：root = [1,2,2,null,3,null,3]
输出：false
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)

    def check(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)


# Initialize the tree node(s)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

# Create an instance of the Solution class
s = Solution()

# Call the isSymmetric method
result = s.isSymmetric(root)
print(result)  # Output: True

# 方法二：迭代
from collections import deque


class Solution2:
    def isSymmetric2(self, root: TreeNode) -> bool:
        return self.check2(root, root)

    def check2(self, u, v):
        q = deque()
        q.append(u)
        q.append(v)
        while q:
            u = q.popleft()
            v = q.popleft()
            if u is None and v is None:
                continue
            if (u is None or v is None) or (u.val != v.val):
                return False

            q.append(u.left)
            q.append(v.right)

            q.append(u.right)
            q.append(v.left)
        return True


# Initialize the tree node(s)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(3)

# Create an instance of the Solution class
s2 = Solution2()

# Call the isSymmetric method
result2 = s2.isSymmetric2(root2)
print(result2)  # Output: True
