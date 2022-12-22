# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 23:29
# @Author  : Walter
# @File    : ListNodeTest.py
# @License : (C)Copyright Walter
# @Desc    :

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# 使用列表构建链表
# def build_linked_list(lst):
#     head = ListNode(lst[0])
#     current = head
#     for i in range(1, len(lst)):
#         current.next = ListNode(lst[i])
#         current = current.next
#     return head
#
# lst = [1, 2, 3]
# head = build_linked_list(lst)
