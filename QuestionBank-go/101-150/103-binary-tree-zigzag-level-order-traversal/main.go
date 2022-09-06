package main

import "fmt"

// zigzag level order traversal
// left to right, then next level right to left
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	result := [][]int{}
	roots := []*TreeNode{root}
	for level := 1; len(roots) > 0; level++ {
		nodes := []*TreeNode{}
		res := []int{}
		for i := 0; i < len(roots); i++ {
			if level%2 == 0 {
				res = append([]int{roots[i].Val}, res...)
				println("level:", level)
				fmt.Printf("%v\n", res)
			} else {
				res = append(res, roots[i].Val)
			}
			if roots[i].Left != nil {
				nodes = append(nodes, roots[i].Left)
			}
			if roots[i].Right != nil {
				nodes = append(nodes, roots[i].Right)
			}
		}
		result = append(result, res)
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
	result := zigzagLevelOrder(n1)
	fmt.Printf("%v\n", result)
}
