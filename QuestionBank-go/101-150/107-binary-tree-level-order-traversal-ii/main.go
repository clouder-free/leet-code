package main

import "fmt"

// level traversal binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderBottom(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	result := [][]int{}
	roots := []*TreeNode{root}
	for len(roots) > 0 {
		nodes := []*TreeNode{}
		res := []int{}
		for i := 0; i < len(roots); i++ {
			res = append(res, roots[i].Val)
			if roots[i].Left != nil {
				nodes = append(nodes, roots[i].Left)
			}
			if roots[i].Right != nil {
				nodes = append(nodes, roots[i].Right)
			}
		}
		result = append([][]int{res}, result...)
		roots = nodes[:]
	}
	return result
}

func main() {
	n5 := &TreeNode{15, nil, nil}
	n4 := &TreeNode{7, nil, nil}
	n3 := &TreeNode{20, n5, n4}
	n2 := &TreeNode{9, nil, nil}
	n1 := &TreeNode{3, n2, n3}
	result := levelOrderBottom(n1)
	fmt.Printf("%v\n", result)

}
