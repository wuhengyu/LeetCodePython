# -*- coding: utf-8 -*-
# @Time    : 2022/12/23 15:13
# @Author  : Walter
# @File    : 160. 相交链表.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
A:a1->a2->c1->c1->c2->c3
B:b1->b2->b3->c1->c2->c3
题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。
自定义评测：
评测系统 的输入如下（你设计的程序 不适用 此输入）：
intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
listA - 第一个链表
listB - 第二个链表
skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。
提示：
listA 中节点数目为 m
listB 中节点数目为 n
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]
进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？
'''
from typing import Optional

import ListNodeTest
# 方法一：哈希集合
# class Solution:
#     def getIntersectionNode(self, headA: ListNodeTest.ListNode, headB: ListNodeTest.ListNode) -> Optional[
#         ListNodeTest.ListNode]:
#         visited = set()
#         temp = headA
#         while (temp != None):
#             visited.add(temp)
#             temp = temp.next
#         temp = headB
#         while (temp != None):
#             if (visited(temp)):
#                 return temp
#             temp = temp.next
#         return None


# 方法二：双指针
# public class Solution {
#     public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
#         if (headA == null || headB == null) {
#             return null;
#         }
#         ListNode pA = headA, pB = headB;
#         while (pA != pB) {
#             pA = pA == null ? headB : pA.next;
#             pB = pB == null ? headA : pB.next;
#         }
#         return pA;
#     }
# }

class Solution:
    def getIntersectionNode(self, headA: ListNodeTest.ListNode, headB: ListNodeTest.ListNode) -> ListNodeTest.ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


node1 = ListNodeTest.ListNode(1)
node2 = ListNodeTest.ListNode(2)
node3 = ListNodeTest.ListNode(3)
node4 = ListNodeTest.ListNode(3)
node5 = ListNodeTest.ListNode(5)
node6 = ListNodeTest.ListNode(5)

node1.next = node3
node3.next = node5
node2.next = node4
node4.next = node6
head1 = Solution().getIntersectionNode(node1, node2)
while head1:
    print(head1.val)
    head2 = head1.next
    print(head1)