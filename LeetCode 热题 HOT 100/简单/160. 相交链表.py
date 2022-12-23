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
# 在这个代码中，我们使用了 Python 中的集合 set 来存储节点是否已被访问过。
# 这样，在遍历链表 B 的时候，如果当前结点出现在集合中，说明它是链表 A 和链表 B 的相交点。
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        visited = set()
        temp = headA
        while temp:
            visited.add(temp)
            temp = temp.next
        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next
        return None

# 测试代码
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node7 = ListNode(7)
node8 = ListNode(8)

node7.next = node8
node8.next = node4

intersection = Solution().getIntersectionNode(node1, node7)
print(intersection.val)  # 输出 4


# 方法二：双指针
# 在这个代码中，我们使用了 Python 中的三元运算符来实现条件赋值。
# 如果两个指针当前结点为空，则将它们设为另一个链表的头结点。否则，就将它们向前移动一步。
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

# 测试代码
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node7 = ListNode(7)
node8 = ListNode(8)

node7.next = node8
node8.next = node4

intersection = Solution().getIntersectionNode(node1, node7)
print(intersection.val)  # 输出 4



class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        # 求出两个链表的长度
        len1, len2 = 0, 0
        p1, p2 = headA, headB
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next

        # 将较长的链表的指针向前移动差值步
        p1, p2 = headA, headB
        if len1 > len2:
            for i in range(len1 - len2):
                p1 = p1.next
        else:
            for i in range(len2 - len1):
                p2 = p2.next

        # 同时向前
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node7 = ListNode(7)
node8 = ListNode(8)

node7.next = node8
node8.next = node4

intersection = Solution().getIntersectionNode(node1, node7)
print(intersection.val) # 输出 4