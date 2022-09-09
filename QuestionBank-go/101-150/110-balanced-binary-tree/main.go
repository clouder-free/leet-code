package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	if treeHeight(root) >= 0 {
		return true
	}
	return false
}

func treeHeight(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := treeHeight(root.Left)
	right := treeHeight(root.Right)
	if left < 0 || right < 0 || math.Abs(float64(left-right)) > 1.0 {
		return -1
	}
	if left < right {
		return right + 1
	} else {
		return left + 1
	}
}

func main() {
	n5 := &TreeNode{7, nil, nil}
	n4 := &TreeNode{15, nil, nil}
	n3 := &TreeNode{20, n4, n5}
	n2 := &TreeNode{9, nil, nil}
	n1 := &TreeNode{3, n2, n3}
	result := isBalanced(n1)
	fmt.Printf("%v\n", result)
}
