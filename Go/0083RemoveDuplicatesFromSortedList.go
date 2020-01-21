/*
 * @Author: wangluyu
 * @Date: 2020-01-19 12:16:34
 * @LastEditors  : wangluyu
 * @LastEditTime : 2020-01-20 19:45:07
 */

package main

import "fmt"

/*
83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2
Example 2:
Input: 1->1->2->3->3
Output: 1->2->3

83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例 1:
输入: 1->1->2
输出: 1->2
示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
*/

// ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// TODO: 删除排序链表中的重复元素
func deleteDuplicates(head *ListNode) *ListNode {
	// lastValue := 0
	node := head
	for node.Next != nil {
		fmt.Println(node.Val)
	}
	return head
}

// func main() {
// }
