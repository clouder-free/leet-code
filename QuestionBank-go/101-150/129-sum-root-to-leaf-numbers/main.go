package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var result int

func sumNumbers(root *TreeNode) int {
	result = 0
	if root == nil {
		return result
	}
	sum(root, root.Val)
	return result
}

func sum(root *TreeNode, temp int) {
	if root.Left == nil && root.Right == nil {
		result += temp
		return
	}
	if root.Left != nil {
		sum(root.Left, temp*10+root.Left.Val)
	}
	if root.Right != nil {
		sum(root.Right, temp*10+root.Right.Val)
	}
}

func main() {
	n3 := &TreeNode{3, nil, nil}
	n2 := &TreeNode{2, nil, nil}
	n1 := &TreeNode{1, n2, n3}
	result := sumNumbers(n1)
	fmt.Printf("result:%v\n", result)
}
