package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	roots := []*TreeNode{root}
	depth := 1
	for len(roots) > 0 {
		nodes := []*TreeNode{}
		for i := 0; i < len(roots); i++ {
			if roots[i].Left == nil && roots[i].Right == nil {
				return depth
			}
			if roots[i].Left != nil {
				nodes = append(nodes, roots[i].Left)
			}
			if roots[i].Right != nil {
				nodes = append(nodes, roots[i].Right)
			}
		}
		roots = nodes[:]
		depth += 1
	}
	return depth
}

func main() {
	n5 := &TreeNode{7, nil, nil}
	n4 := &TreeNode{15, nil, nil}
	n3 := &TreeNode{20, n4, n5}
	n2 := &TreeNode{9, nil, nil}
	n1 := &TreeNode{3, n2, n3}
	result := minDepth(n1)
	fmt.Printf("%v\n", result)
}
