# -*- coding: utf-8 -*-
# Time    : 2023/6/5 0:01
# Author  : Walter
# File    : 链表demo.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

while root:
    print(root.val)
    root = root.right

# while root:
#     print(root.val)
#     root = root.left
