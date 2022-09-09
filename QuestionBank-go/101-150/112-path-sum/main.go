package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	return pathSum(root, root.Val, targetSum)
}

func pathSum(root *TreeNode, current int, targetSum int) bool {
	if root.Left == nil && root.Right == nil {
		if current == targetSum {
			return true
		}
	} else {
		if root.Left != nil && pathSum(root.Left, current+root.Left.Val, targetSum) {
			return true
		}
		if root.Right != nil && pathSum(root.Right, current+root.Right.Val, targetSum) {
			return true
		}
	}
	return false
}

func main() {
	n9 := &TreeNode{1, nil, nil}
	n8 := &TreeNode{7, nil, nil}
	n7 := &TreeNode{2, nil, nil}
	n6 := &TreeNode{4, nil, n9}
	n5 := &TreeNode{13, nil, nil}
	n4 := &TreeNode{11, n8, n7}
	n3 := &TreeNode{8, n5, n6}
	n2 := &TreeNode{4, n4, nil}
	n1 := &TreeNode{5, n2, n3}
	result := hasPathSum(n1, 22)
	fmt.Printf("result:%v\n", result)
}
