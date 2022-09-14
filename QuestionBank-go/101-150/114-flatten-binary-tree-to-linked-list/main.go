package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {
	for root != nil {
		if root.Left != nil {
			r := root.Left
			for r.Right != nil {
				r = r.Right
			}
			r.Right = root.Right
			root.Right = root.Left
			root.Left = nil
		}
		root = root.Right
	}

}
