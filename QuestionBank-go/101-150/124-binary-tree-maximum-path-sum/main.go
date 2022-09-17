package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var result int

func maxPathSum(root *TreeNode) int {
	result = math.MinInt16
	pathSum(root)
	return result
}

func pathSum(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := pathSum(root.Left)
	right := pathSum(root.Right)
	if left < 0 {
		left = 0
	}
	if right < 0 {
		right = 0
	}
	if result < left+right+root.Val {
		result = left + right + root.Val
	}
	if left < right {
		return right + root.Val
	} else {
		return left + root.Val
	}
}

func main() {

}
