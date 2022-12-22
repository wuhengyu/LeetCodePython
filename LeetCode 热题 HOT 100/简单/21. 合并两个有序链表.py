# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 23:14
# @Author  : Walter
# @File    : 21. 合并两个有序链表.py
# @License : (C)Copyright Walter
# @Desc    :
'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
红1->红2->红4
紫1->紫3->紫4
紫1->红1->红2->紫3->红4->紫4
示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：
输入：l1 = [], l2 = []
输出：[]
示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
'''
import ListNodeTest
class Solution:
    def mergeTwoLists(self, l1: ListNodeTest.ListNode, l2: ListNodeTest.ListNode) -> ListNodeTest.ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


node1 = ListNodeTest.ListNode(1)
node2 = ListNodeTest.ListNode(2)
node3 = ListNodeTest.ListNode(3)
node4 = ListNodeTest.ListNode(4)
node5 = ListNodeTest.ListNode(5)
node6 = ListNodeTest.ListNode(6)

node1.next = node3
node3.next = node5
node2.next = node4
node4.next = node6

head = Solution().mergeTwoLists(node1, node2)
while head:
    print(head.val)
    head = head.next
    print(head)
