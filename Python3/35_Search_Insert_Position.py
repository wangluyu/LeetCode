#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Desc: 35. 搜索插入位置 （简单）
Author: wangluyu
Date: 2020/1/14
"""
from typing import List


class Solution:
    """
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
    You may assume no duplicates in the array.
    Example 1:
    Input: [1,3,5,6], 5
    Output: 2
    Example 2:
    Input: [1,3,5,6], 2
    Output: 1
    Example 3:
    Input: [1,3,5,6], 7
    Output: 4
    Example 4:
    Input: [1,3,5,6], 0
    Output: 0
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素。
    示例 1:
        输入: [1,3,5,6], 5
        输出: 2
    示例 2:
        输入: [1,3,5,6], 2
        输出: 1
    示例 3:
        输入: [1,3,5,6], 7
        输出: 4
    示例 4:
        输入: [1,3,5,6], 0
        输出: 0
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        return self.binary_search(nums, 0, len(nums) -1, target)

    def binary_search(self, arr, start, end, target):
        if start > end:
            return start if arr[start] > target else end
        mid = start + int((end - start) / 2)
        if arr[mid] > target:
            return self.binary_search(arr, start, mid - 1, target)
        if arr[mid] < target:
            return self.binary_search(arr, mid + 1, end, target)
        return mid


if __name__ == '__main__':
    nums = [1,3,5,6,9]
    target = 7
    s = Solution()
    print(s.searchInsert(nums, target))

