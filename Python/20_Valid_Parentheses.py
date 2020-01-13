#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Desc: 20. 有效的括号 (简单)
Author: wangluyu
Date: 2020/1/13
"""


class Solution:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    Example 1:
        Input: "()"
        Output: true
    Example 2:
        Input: "()[]{}"
        Output: true
    Example 3:
        Input: "(]"
        Output: false
    Example 4:
        Input: "([)]"
        Output: false
    Example 5:
        Input: "{[]}"
        Output: true
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
    示例 1:
        输入: "()"
        输出: true
    示例 2:
        输入: "()[]{}"
        输出: true
    示例 3:
        输入: "(]"
        输出: false
    示例 4:
        输入: "([)]"
        输出: false
    示例 5:
        输入: "{[]}"
        输出: true
    """
    def isValid(self, s: str) -> bool:
        open_brackets_stack = []
        brackets_dict = {'(': ')', '[': ']', '{': '}'}
        for value in s:
            if brackets_dict.get(value, '') != "":
                open_brackets_stack.append(value)
            elif len(open_brackets_stack) == 0 or brackets_dict[open_brackets_stack.pop()] != value:
                return False
        return open_brackets_stack == []


if __name__ == '__main__':
    str = "([)]"
    s = Solution()
    print(s.isValid(str))