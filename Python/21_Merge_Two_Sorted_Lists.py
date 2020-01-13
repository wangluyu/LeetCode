#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Desc: 21. 合并两个有序链表 (简单)
Author: wangluyu
Date: 2020/1/13
"""

from util import Link


class ListNode(Link.ListNode):
    def __init__(self, x):
        super(ListNode, self).__init__(x)

class Solution:
    """
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
    Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
    示例：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        head = node
        while l1 and l2:
            if l1.val < l2.val:
                tmp = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp = ListNode(l2.val)
                l2 = l2.next
            node.next = tmp
            node = tmp
        if l1 is not None:
            node.next = l1
        elif l2 is not None:
            node.next = l2
        return head.next


if __name__ == '__main__':
    s = Solution()
    link1 = Link.list_to_link([1,2,4])
    link2 = Link.list_to_link([1,3,4])
    Link.print_link(s.mergeTwoLists(link1, link2))
