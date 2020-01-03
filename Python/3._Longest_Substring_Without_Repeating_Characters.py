#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Author: wangluyu
Date: 2020/1/3
"""


class Solution:
    """
    3. 无重复字符的最长子串
    Given a string, find the length of the longest substring without repeating characters.
    Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    示例 1:
    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:
    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:
    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        while len(s) > 0:
            index = len(s)
            sub_s = ""
            for i, v in enumerate(s):
                if v not in sub_s:
                    sub_s += v
                else:
                    index = sub_s.index(v)
                    break
            max_len = max(max_len, len(sub_s))
            s = s[index + 1:]
        return max_len


if __name__ == '__main__':
    _s = Solution()
    print(_s.lengthOfLongestSubstring("pwwkew"))
