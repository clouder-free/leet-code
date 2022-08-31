package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	// left->root->right
	result := []int{}
	if root != nil {
		result = append(result, inorderTraversal(root.Left)...)
		result = append(result, root.Val)
		result = append(result, inorderTraversal(root.Right)...)
	}
	return result
}

func inorderTraversal2(root *TreeNode) []int {
	result := []int{}
	nodes := []*TreeNode{}
	for root != nil || len(nodes) > 0 {
		if root != nil {
			nodes = append(nodes, root)
			root = root.Left
		} else {
			root = nodes[len(nodes)-1]
			result = append(result, root.Val)
			root = root.Right
			nodes = nodes[:len(nodes)-1]
		}
	}
	return result
}

func main() {
	n3 := &TreeNode{3, nil, nil}
	n2 := &TreeNode{2, nil, nil}
	n1 := &TreeNode{1, nil, nil}
	n1.Right = n2
	n2.Left = n3
	r := inorderTraversal2(n1)
	fmt.Printf("r:%v\n", r)
}
