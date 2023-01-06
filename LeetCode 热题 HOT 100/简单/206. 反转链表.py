# -*- coding: utf-8 -*-
# @Time    : 2022/12/30 0:03
# @Author  : Walter
# @File    : 206. 反转链表.py
# @License : (C)Copyright Walter
# @Desc    :

'''
你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：
输入：head = [1,2]
输出：[2,1]
示例 3：
输入：head = []
输出：[]
'''

'''
该函数接受一个ListNode调用的对象head并将反向链表作为ListNode对象返回。
该函数通过遍历链表并反转每个节点的指针来工作。prev变量跟踪前一个节点，而变量curr用于遍历列表。
该next变量用于存储指针反转前的下一个节点。循环一直持续到curr节点变为None，此时返回反向链表。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


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

reverse = Solution().reverseList(node1)
print(reverse.val)

'''
该函数接受一个ListNode对象作为输入，并将反向链表作为一个ListNode对象返回。该函数使用递归通过更改列表中节点的指针来反转链表。
递归的基本情况是当输入head为None或head.next时None，这意味着链表为空或只有一个元素。在这些情况下，该函数只返回head反向列表。
next对于所有其他情况，该函数以 的节点作为输入调用自身，head并将结果存储在一个名为 的新变量中new_head。然后，
它将to的节点指针设置为指向自己next，并设置to的指针。最后，它返回反向列表。nextheadheadnextheadNonenew_head
'''


class Solution2:
    def reverseList2(self, head: ListNode) -> ListNode:
        # 递归终止条件是当前为空，或者下一个节点为空
        if head is None or head.next is None:
            return head

        # 这里的new_head就是最后一个节点
        new_head = self.reverseList2(head.next)
        print(new_head)
        head.next.next = head
        print(head.next.next)
        head.next = None
        print(new_head)
        # 每层递归函数都返回new_head，也就是最后一个节点
        return new_head


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

reverse2 = Solution2().reverseList2(node1)
print(reverse2.val)
