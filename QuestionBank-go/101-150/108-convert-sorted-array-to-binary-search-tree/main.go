package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	if len(nums) == 1 {
		return &TreeNode{nums[0], nil, nil}
	}
	index := len(nums) / 2
	root := &TreeNode{nums[index], nil, nil}
	root.Left = sortedArrayToBST(nums[:index])
	root.Right = sortedArrayToBST(nums[index+1:])
	return root
}

func printTree(root *TreeNode) {
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
		roots = nodes[:]
		fmt.Printf("%v\n", res)
	}
}

func main() {
	nums := []int{-10, -3, 0, 5, 9}
	result := sortedArrayToBST(nums)
	printTree(result)
}
