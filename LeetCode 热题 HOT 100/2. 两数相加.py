# -*- coding: utf-8 -*-
# @Time    : 2022/11/12 0:26
# @Author  : Walter
# @File    : 2. 两数相加.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
'''


class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# 创建链表
def build_link(nums):
    li = cur = ListNode()
    for i in nums:
        cur.next = ListNode(i)
        cur = cur.next
    return li.next

def printNode(node):
    while node:
        # print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
        print(' value: ', node.val)
        node = node.next


class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry

            if l1: l1, val = l1.next, l1.val + val
            if l2: l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)

        print(printNode(head))
        return head.next


nums1 = [2, 4, 3]
nums2 = [5, 6, 4]
l1 = build_link(nums1)
l2 = build_link(nums2)
print(Solution().addTwoNumbers(l1, l2))
