#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Desc: 14. 最长公共前缀 (简单)
Author: wangluyu
Date: 2020/1/13
"""
from typing import List


class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"
    Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    Note:
    All given inputs are in lowercase letters a-z.
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
    示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"
    示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
    说明:
    所有输入只包含小写字母 a-z 。
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            strlen = min(len(prefix), len(strs[i]))
            tmp_prefix = ""
            for j in range(strlen):
                if prefix[j] == strs[i][j]:
                    tmp_prefix += prefix[j]
                else:
                    break
            if tmp_prefix == "":
                return ""
            prefix = tmp_prefix
        return prefix


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))