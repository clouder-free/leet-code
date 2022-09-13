package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var result [][]int

func pathSum(root *TreeNode, targetSum int) [][]int {
	// init
	result = [][]int{}
	if root == nil {
		return result
	}
	path(root, []int{root.Val}[:], root.Val, targetSum)
	return result
}

func path(root *TreeNode, res []int, current, targetSum int) {
	if root.Left == nil && root.Right == nil {
		// fmt.Printf("root:%v res:%v current:%v \n", root.Val, res, current)
		if current == targetSum {
			tmp := make([]int, len(res))
			copy(tmp, res)
			result = append(result, tmp)
		}
	} else {
		if root.Left != nil {
			path(root.Left, append(res, root.Left.Val), current+root.Left.Val, targetSum)
		}
		if root.Right != nil {
			path(root.Right, append(res, root.Right.Val), current+root.Right.Val, targetSum)
		}
	}
}

func main() {
	n9 := &TreeNode{1, nil, nil}
	n8 := &TreeNode{5, nil, nil}
	n7 := &TreeNode{7, nil, nil}
	n6 := &TreeNode{2, nil, nil}
	n5 := &TreeNode{4, n8, n9}
	n4 := &TreeNode{13, nil, nil}
	n3 := &TreeNode{11, n7, n6}
	n2 := &TreeNode{8, n4, n5}
	n1 := &TreeNode{4, n3, nil}
	n0 := &TreeNode{5, n1, n2}
	result0 := pathSum(n0, 22)
	fmt.Printf("result:%v\n", result0)
}
