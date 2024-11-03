# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 23:42
# @Author  : Walter
# @File    : 94. 二叉树的中序遍历.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给定一个二叉树的根节点 root ，返回 它的 中序遍历 。
示例 1：
    1
        2
    3
输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：
输入：root = []
输出：[]
示例 3：
输入：root = [1]
输出：[1]

中序遍历首先遍历左子树，然后访问根结点，最后遍历右子树。若二叉树为空则结束返回，否则：
（1）中序遍历左子树
（2）访问根结点
（3）中序遍历右子树

首先我们需要了解什么是二叉树的中序遍历：按照访问左子树——根节点——右子树的方式遍历这棵树，
而在访问左子树或者右子树的时候我们按照同样的方式遍历，直到遍历完整棵树。因此整个遍历过程天然具有递归的性质，
我们可以直接用递归函数来模拟这一过程。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法一：递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root: TreeNode, res: List[int]) -> None:
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


# Initialize the tree node(s)
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create an instance of the Solution class
s = Solution()

# Call the isSymmetric method
result = s.inorderTraversal(root)
print(result)  # Output: True


# 方法二：迭代
class Solution2:
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        stk = []
        while root is not None or len(stk) > 0:
            while root is not None:
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res


# Initialize the tree node(s)
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create an instance of the Solution class
s2 = Solution2()

# Call the isSymmetric method
result2 = s2.inorderTraversal2(root)
print(result2)  # Output: True


# 方法三：Morris 中序遍历
class Solution3:
    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        res = []
        predecessor = None

        while root is not None:
            if root.left is not None:
                predecessor = root.left
                while predecessor.right is not None and predecessor.right != root:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    predecessor.right = None
                    root = root.right
            else:
                res.append(root.val)
                root = root.right
        return res


# Initialize the tree node(s)
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create an instance of the Solution class
s3 = Solution3()

# Call the isSymmetric method
result3 = s3.inorderTraversal3(root)
print(result3)  # Output: True
