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

func isValidBST(root *TreeNode) bool {
	return validBST(root, math.MinInt64, math.MaxInt64)
}

func validBST(node *TreeNode, minValue int, maxValue int) bool {
	if node == nil {
		return true
	}
	if minValue >= node.Val || maxValue <= node.Val {
		return false
	}
	if !validBST(node.Left, minValue, node.Val) {
		return false
	}
	if !validBST(node.Right, node.Val, maxValue) {
		return false
	}
	return true
}

func main() {
	n3 := &TreeNode{3, nil, nil}
	n7 := &TreeNode{7, nil, nil}
	n6 := &TreeNode{6, n3, n7}
	n4 := &TreeNode{4, nil, nil}
	n5 := &TreeNode{5, n4, n6}
	result := isValidBST(n5)
	fmt.Println("result:", result)
}
