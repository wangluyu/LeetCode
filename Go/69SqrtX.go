/*
 * @Author: wangluyu
 * @Date: 2020-01-17 15:38:47
 * @LastEditors  : wangluyu
 * @LastEditTime : 2020-01-17 16:28:07
 */

package main

/*
69. Sqrt(x)
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
Example 1:
	Input: 4
	Output: 2
Example 2:
	Input: 8
	Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

69. x 的平方根
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
示例 1:
	输入: 4
	输出: 2
示例 2:
	输入: 8
	输出: 2
说明: 8 的平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
*/
func mySqrt(x int) int {
	if x <= 1 {
		return x
	}
	y := x / 2
	for y*y > x {
		y = (y + x/y) / 2
	}
	return int(y)
}

// func main() {
// 	fmt.Println(mySqrt(90))
// }
