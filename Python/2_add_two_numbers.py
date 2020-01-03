#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: wangluyu
Date: 2020/1/3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.add(l1, l2)

    def add(self, l1, l2, carry=0):
        if l1 is None and l2 is None:
            return ListNode(1) if carry > 0 else None
        l1 = l1 if isinstance(l1, ListNode) else ListNode(0)
        l2 = l2 if isinstance(l2, ListNode) else ListNode(0)
        val = l1.val + l2.val + carry
        l = ListNode(val % 10)
        l.next = self.add(l1.next, l2.next, int(val/10))
        return l


if __name__ == '__main__':
    l11 = ListNode(8)
    l11.next = ListNode(1)
    _s = Solution()
    ln = _s.addTwoNumbers(l11, ListNode(0))
    while isinstance(ln, ListNode):
        print(ln.val)
        ln = ln.next

