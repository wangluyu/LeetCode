/*
 * @Author: wangluyu
 * @Date: 2020-01-17 16:28:21
 * @LastEditors  : wangluyu
 * @LastEditTime : 2020-01-17 17:23:11
 */

package main

/*
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
*/

// 斐波那契
// 时间复杂度O(n) 空间复杂度O(1)
func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	// sum => f(n), x => f(n-2), y => f(n-1)
	sum, x, y := 0, 1, 2
	for index := 0; index < n-2; index++ {
		// f(n) = f(n-1) + f(n-2)
		sum = x + y
		x, y = y, sum
	}
	return sum
}

// func main() {
// 	fmt.Println(climbStairs(5))
// }
