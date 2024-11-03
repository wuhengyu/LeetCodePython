# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 16:14
# @Author  : Walter
# @File    : 104. 二叉树的最大深度.py
# @License : (C)Copyright Walter
# @Desc    :
'''
定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明:叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。
'''
import collections
from typing import Optional
import BinaryTree

class Solution:
    def maxDepth(self, root: BinaryTree.TreeNode) -> int:
        if not root:
            return 0
        res = 0  # 保存结果
        q = collections.deque()
        q.append(root)  # 根节点入队
        while q:
            res += 1  # 能进入循环，说明当前层是有节点的，深度+1
            size = len(q)  # 当前层节点的个数
            for _ in range(size):
                cur = q.popleft()  # 出队
                if cur.lchild: q.append(cur.lchild)  # 左子树入队
                if cur.rchild: q.append(cur.rchild)  # 右子树入队

        return res


class Solution2:
    def maxDepth(self, root: Optional[BinaryTree.TreeNode]) -> int:
        # def recur(root): # DFS
        #     if not root:
        #         return 0
        #     left = recur(root.left)
        #     right = recur(root.right)
        #     return max(left, right)+1
        # return recur(root)

        # BFS
        if not root:
            return 0
        deque = collections.deque([root])
        Len = 0
        while deque:
            for _ in range(len(deque)):
                tmp = deque.popleft()
                if tmp.lchild:
                    deque.append(tmp.lchild)
                if tmp.rchild:
                    deque.append(tmp.rchild)
            Len += 1
        return Len

class Solution3(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [root]
        height = 0
        while queue:
            currentSize = len(queue)
            for i in range(currentSize):
                node = queue.pop(0)
                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)
            height += 1
        return height


Root = None
strs = "abc##d##e"  # 前序遍历扩展的二叉树序列
vals = list(strs)
Roots = BinaryTree.Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
print(Solution().maxDepth(Roots))
print(Solution2().maxDepth(Roots))
print(Solution3().maxDepth(Roots))