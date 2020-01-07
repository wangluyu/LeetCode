#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Desc: 4. 寻找两个有序数组的中位数
Author: wangluyu
Date: 2020/1/3
"""
from typing import List

#TODO: 有时间优化下
class Solution:
    """
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    You may assume nums1 and nums2 cannot be both empty.
    Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0
    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    The median is (2 + 3)/2 = 2.5
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
    示例 1:
    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0
    示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_list = []
        index1, index2 = 0, 0
        for v1 in nums1:
            if len(nums2) == index2:
                break
            for v2 in nums2[index2:]:
                if v1 < v2:
                    num_list.append(v1)
                    index1 += 1
                    break
                elif v1 == v2:
                    num_list.append(v1)
                    num_list.append(v2)
                    index1 += 1
                    index2 += 1
                    break
                else:
                    num_list.append(v2)
                    index2 += 1
        if index1 < len(nums1):
            num_list += nums1[index1:]
        elif index2 < len(nums2):
            num_list += nums2[index2:]
        # print(num_list)
        index = int(len(num_list) / 2)
        if len(num_list) % 2 == 0:  # 偶数个数
            return (num_list[index] + num_list[index - 1]) / 2
        else:
            return num_list[index]

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return median(nums2)
        elif len(nums2) == 0:
            return median(nums1)
        length = len(nums1) + len(nums2)
        index = int(length/2) + 1
        num_list = []
        # 标记num1, num2已排序的index
        index1, index2 = 0, 0
        for v1 in nums1:
            if (index1 + index2) == index:
                break
            if len(nums2) == index2:
                break
            for v2 in nums2[index2:]:
                if v1 < v2:
                    num_list.append(v1)
                    index1 += 1
                    break
                else:
                    num_list.append(v2)
                    index2 += 1
                if (index1 + index2) == index:
                    break
        # 没排完
        if (index1 + index2) < index:
            if index1 < len(nums1):
                num_list += nums1[index1:index - index2]
            elif index2 < len(nums2):
                num_list += nums2[index2:index - index1]
        print(num_list)
        if length % 2 == 0:
            return (num_list[-1] + num_list[-2]) / 2
        else:
            return num_list[-1]

def median(num_list):
    """
    :param args:
    :return:
    """
    index = int(len(num_list) / 2)
    if len(num_list) % 2 == 0:  # 偶数个数
        return (num_list[index] + num_list[index - 1]) / 2
    else:
        return num_list[index]


if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [1,2]
    _s = Solution()
    print(_s.findMedianSortedArrays(nums1, nums2))
