#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Desc: 9. 回文数
Author: wangluyu
Date: 2020/1/9
"""


class Solution:
    """
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
    Example 1:
        Input: 121
        Output: true
    Example 2:
        Input: -121
        Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    Example 3:
        Input: 10
        Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    Follow up:
    Coud you solve it without converting the integer to a string?
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
    示例 1:
        输入: 121
        输出: true
    示例 2:
        输入: -121
        输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
    示例 3:
        输入: 10
        输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。
    进阶:
    你能不将整数转为字符串来解决这个问题吗？
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        y = 0
        while num > 0:
            y = (y * 10) + (num % 10)
            num = int(num / 10)
        if y == x:
            return True

    def isPalindrome1(self, x: int) -> bool:
        # 官方解法
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = 0
        # 只反转一半数字
        while x > y:
            y = (y * 10) + (x % 10)
            x = int(x / 10)
        return x == y or x == int(y/10)


if __name__ == '__main__':
    x = 10
    s = Solution()
    print(s.isPalindrome1(x))
