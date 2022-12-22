# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 13:04
# @Author  : Walter
# @File    : BinaryTree.py
# @License : (C)Copyright Walter
# @Desc    :

class TreeNode():  # 二叉树节点
    def __init__(self, val, lchild=None, rchild=None):
        self.val = val  # 二叉树的节点值
        self.lchild = lchild  # 左孩子
        self.rchild = rchild  # 右孩子


def Creat_Tree(Root, vals):
    if len(vals) == 0:  # 终止条件：val用完了
        return Root
    if vals[0] != '#':  # 本层需要干的就是构建Root、Root.lchild、Root.rchild三个节点。
        Root = TreeNode(vals[0])
        vals.pop(0)
        Root.lchild = Creat_Tree(Root.lchild, vals)
        Root.rchild = Creat_Tree(Root.rchild, vals)
        return Root  # 本次递归要返回给上一次的本层构造好的树的根节点
    else:
        Root = None
        vals.pop(0)
        return Root  # 本次递归要返回给上一次的本层构造好的树的根节点


if __name__ == '__main__':
    Root = None
    strs = "abc##d##e##"  # 前序遍历扩展的二叉树序列
    vals = list(strs)
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    print(Roots)
