package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)
	if leftDepth > rightDepth {
		return leftDepth + 1
	} else {
		return rightDepth + 1
	}
}

func main() {
	n5 := &TreeNode{15, nil, nil}
	n4 := &TreeNode{7, nil, nil}
	n3 := &TreeNode{20, n5, n4}
	n2 := &TreeNode{9, nil, nil}
	n1 := &TreeNode{3, n2, n3}
	result := maxDepth(n1)
	fmt.Printf("%v\n", result)
}
