# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 20:36
# @Author  : Walter
# @File    : 链表基础操作.py
# @License : (C)Copyright Walter
# @Desc    :

class Node(object):
    def __init__(self):
        self.val = None
        self.next = None


class Node_handle():
    def __init__(self):
        self.cur_node = None

    # 增加
    def add(self, data):
        node = Node()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    # 打印
    def printNode(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next


if __name__ == "__main__":
    l1 = Node()
    ListNode = Node_handle()
    l1_list = [1, 8, 3]
    for i in l1_list:
        l1 = ListNode.add(i)
    ListNode.printNode(l1)
