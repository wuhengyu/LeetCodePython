# -*- coding: utf-8 -*-
# Time : 2023/6/9 18:16
# Author : Walter
# File : 708. 循环有序列表的插入.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc :
'''
给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素insertVal ，使这个列表仍然是循环非降序的。
给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个节点。否则，请返回原先给定的节点。

示例 1：
输入：head = [3,4,1], insertVal = 2
输出：[3,4,1,2]
解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3 。

示例 2：
输入：head = [], insertVal = 1
输出：[1]
解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。

示例 3：
输入：head = [1], insertVal = 0
输出：[1,0]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一：一次遍历
class Solution:
    def insert(self, head: 'ListNode', insertVal: int) -> 'ListNode':
        node = ListNode(insertVal)
        if head is None:
            node.next = node
            return node
        if head.next == head:
            head.next = node
            node.next = head
            return head
        curr = head
        next = head.next
        while next != head:
            if curr.val <= insertVal <= next.val:
                break
            if curr.val > next.val:
                if insertVal > curr.val or insertVal < next.val:
                    break
            curr = curr.next
            next = next.next
        curr.next = node
        node.next = next
        return head


# root1 = ListNode(3, ListNode(4, ListNode(1)))
# print(Solution().insert(root1, 2))

head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(1)
head.next.next.next = head

solution = Solution()
new_head = solution.insert(head, 2)
while new_head.next != head:
    print(new_head.val)
    new_head = new_head.next