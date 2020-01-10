#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Desc: 7. 整数反转
Author: wangluyu
Date: 2020/1/8
"""


class Solution:
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    Example 1:
        Input: 123
        Output: 321
    Example 2:
        Input: -123
        Output: -321
    Example 3:
        Input: 120
        Output: 21
    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
    示例 1:
        输入: 123
        输出: 321
    示例 2:
        输入: -123
        输出: -321
    示例 3:
        输入: 120
        输出: 21
    注意:
    假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
    """
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        num = num if x > 0 else -num
        if num > 2147483647 or num < -2147483648:
            return 0
        return num

    def reverse1(self, x: int) -> int:
        flag = x > 0
        x = x if x > 0 else -x
        num = 0
        while x > 0:
            num = (num * 10) + x % 10
            x = int(x / 10)
        num = num if flag else -num
        if num > 2147483647 or num < -2147483648:
            return 0
        return int(num)


if __name__ == '__main__':
    x = -123
    s = Solution()
    print(s.reverse1(x))
