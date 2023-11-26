# -*- coding: utf-8 -*-
# Time    : 2023/11/8 22:53
# Author  : Walter
# File    : 双链表.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_reverse(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()


# 创建一个双链表对象
dll = DoublyLinkedList()

# 添加节点到双链表
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

# 正向打印链表中的节点
dll.display()

# 反向打印链表中的节点
dll.display_reverse()
