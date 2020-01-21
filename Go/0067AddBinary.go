/*
 * @Author: wangluyu
 * @Date: 2020-01-17 13:13:38
 * @LastEditors  : wangluyu
 * @LastEditTime : 2020-01-17 16:01:02
 */

package main

import "strconv"

/*
67. Add Binary (simple)
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

67. 二进制求和 (简单)
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。
示例 1:
输入: a = "11", b = "1"
输出: "100"
示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
*/

func addBinary(a string, b string) string {
	var s string
	carry := 0
	for i, j := len(a)-1, len(b)-1; i >= 0 || j >= 0; i, j = i-1, j-1 {
		tmp1, tmp2 := 0, 0
		if i >= 0 {
			tmp1 = int(a[i] - '0')
		}
		if j >= 0 {
			tmp2 = int(b[j] - '0')
		}
		sum := carry + tmp1 + tmp2
		if sum >= 2 {
			carry = 1
		} else {
			carry = 0
		}
		sum = sum % 2
		s = strconv.Itoa(sum) + s
	}
	if carry == 1 {
		s = "1" + s
	}
	return s
}

// func main() {
// 	fmt.Println(addBinary("1010", "1011"))
// }
