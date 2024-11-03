# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 12:16
# @Author  : Walter
# @File    : 543. 二叉树的直径.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回3, 它的长度是路径 [4,2,1,3] 或者[5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。

一条路径的长度为该路径经过的节点数减一，所以求直径（即求路径长度的最大值）等效于求路径经过节点数的最大值减一。
'''

import BinaryTree
class Solution:
    def diameterOfBinaryTree(self, root: BinaryTree.TreeNode) -> int:
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.lchild)
            # 右儿子为根的子树的深度
            R = depth(node.rchild)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

Root = None
strs = "abc##d##e##"  # 前序遍历扩展的二叉树序列
vals = list(strs)
Roots = BinaryTree.Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
print(Solution().diameterOfBinaryTree(Roots))