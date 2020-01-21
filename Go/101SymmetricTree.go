/*
 * @Author: wangluyu
 * @Date: 2020-01-21 15:37:06
 * @LastEditors  : wangluyu
 * @LastEditTime : 2020-01-21 15:46:41
 */

package main

// TreeNode is 二叉树
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
*/
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return isMirrorTree(root.Left, root.Right)
}

func isMirrorTree(p *TreeNode, q *TreeNode) bool {
	// 都为空 证明已经遍历到最后一个节点都相等 return true
	if p == nil && q == nil {
		return true
	}
	// 只有一个节点为空 证明节点数不相等 return false
	if p == nil || q == nil {
		return false
	}
	// 节点都不为空 但值不同 return false
	if p.Val != q.Val {
		return false
	}
	return isMirrorTree(p.Left, q.Right) && isMirrorTree(p.Right, q.Left)
}
