/*
 * @Author: wangluyu
 * @Date: 2020-01-19 19:27:02
 * @LastEditors  : wangluyu
 * @LastEditTime : 2020-01-20 20:00:56
 */

package main

import "fmt"

/**
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

88. 合并两个有序数组
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
*/

func merge(nums1 []int, m int, nums2 []int, n int) []int {
	m,n = m - 1,n - 1
	z := m + n + 1
	for m >= 0 || n >= 0 {
		if m < 0 {
			nums1[z] = nums2[n]
			n--
		} else if n < 0 {
			nums1[z] = nums1[m]
			m--
		} else if nums1[m] > nums2[n] {
			nums1[z] = nums1[m]
			m--
		} else {
			nums1[z] = nums2[n]
			n--
		}
		z--
	}
	return nums1
}

// func main() {
// 	nums1 := []int{1, 2, 3, 0, 0, 0}
// 	nums2 := []int{2, 5, 6}
// 	fmt.Println(merge(nums1, 3, nums2, len(nums2)))
// }
