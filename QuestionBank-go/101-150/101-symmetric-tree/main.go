package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	// symmetric tree
	return symmetricTree(root.Left, root.Right)
}

func symmetricTree(left *TreeNode, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	}
	if (left == nil && right != nil) || (left != nil && right == nil) {
		return false
	}
	if left.Val != right.Val {
		return false
	}
	return symmetricTree(left.Left, right.Right) && symmetricTree(left.Right, right.Left)
}

func main() {
	n1 := &TreeNode{1, nil, nil}
	n21 := &TreeNode{2, nil, nil}
	n22 := &TreeNode{2, nil, nil}
	n31 := &TreeNode{3, nil, nil}
	n32 := &TreeNode{3, nil, nil}
	n41 := &TreeNode{4, nil, nil}
	n42 := &TreeNode{4, nil, nil}
	n21.Left = n31
	n21.Right = n41
	n22.Left = n42
	n22.Right = n32
	n1.Left = n21
	n1.Right = n22
	result := isSymmetric(n1)
	fmt.Println("result:", result)
}
