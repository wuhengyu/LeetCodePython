# -*- coding: utf-8 -*-
# @Time    : 2022/12/23 15:48
# @Author  : Walter
# @File    : 234. 回文链表.py
# @License : (C)Copyright Walter
# @Desc    :
'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
1->2->2->1
输入：head = [1,2,2,1]
输出：true
1->2
输入：head = [1,2]
输出：false
提示：
链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9
'''
import ListNodeTest
# 方法一：将值复制到数组中后用双指针法
class Solution:
    def isPalindrome(self, head: ListNodeTest.ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


node1 = ListNodeTest.ListNode(1)
node3 = ListNodeTest.ListNode(2)
node5 = ListNodeTest.ListNode(2)
node7 = ListNodeTest.ListNode(1)

node1.next = node3
node3.next = node5
node5.next = node7
head1 = Solution().isPalindrome(node1)
print(head1)

# 方法二：递归
class Solution:
    def isPalindrome(self, head: ListNodeTest.ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

node1 = ListNodeTest.ListNode(1)
node3 = ListNodeTest.ListNode(2)
node5 = ListNodeTest.ListNode(2)
node7 = ListNodeTest.ListNode(1)

node1.next = node3
node3.next = node5
node5.next = node7
head2 = Solution().isPalindrome(node1)
print(head2)

# 方法三：快慢指针
class Solution:

    def isPalindrome(self, head: ListNodeTest.ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

node1 = ListNodeTest.ListNode(1)
node3 = ListNodeTest.ListNode(2)
node5 = ListNodeTest.ListNode(2)
node7 = ListNodeTest.ListNode(1)

node1.next = node3
node3.next = node5
node5.next = node7
head3 = Solution().isPalindrome(node1)
print(head3)
