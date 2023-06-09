# -*- coding: utf-8 -*-
# Time : 2023/6/9 16:25
# Author : Walter
# File : 369. 给单链表加一.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :
'''
给定一个用链表表示的非负整数， 然后将这个整数再加上 1 。
这些数字的存储是这样的：最高位有效的数字位于链表的首位head。

示例 1:
输入: head = [1,2,3]
输出: [1,2,4]

示例2:
输入: head = [0]
输出: [1]

提示：
链表中的节点数在[1, 100]的范围内。
0 <= Node.val <= 9
由链表表示的数字不包含前导零，除了零本身。
'''

# 解题思路：
# 初始化哨兵节点 ListNode(0)，同时将它设为新的头节点：sentinel.next = head。
# 找到最靠右的数值不为 9 的节点。
# 将该节点的数值加 1。
# 将该节点之后所有节点数值改为 0。
# 如果哨兵节点的数值为 1，直接返回哨兵节点，否则返回原始头节点 sentinel.next。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一：哨兵头节点
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        not_nine.val += 1
        not_nine = not_nine.next

        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next


print(Solution().plusOne(ListNode(1, ListNode(2, ListNode(3)))).val)

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
print(Solution().plusOne(root).val)
