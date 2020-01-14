#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Desc: 
Author: wangluyu
Date: 2020/1/13
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_link(arr) -> ListNode:
    ln = ListNode(arr[0])
    head = ln
    for i in range(1, len(arr)):
        tmp = ListNode(arr[i])
        ln.next = tmp
        ln = tmp
    return head


def print_link(link):
    l = []
    while link:
        l.append(link.val)
        link = link.next
    print(' -> '.join(map(str, l)))
