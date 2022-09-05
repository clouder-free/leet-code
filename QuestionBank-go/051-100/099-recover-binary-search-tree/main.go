package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recoverTree(root *TreeNode) {
	// middle traverse the binary search tree, then we get the increase list
	// if there are two nodes mistaken, the increase order dismiss
	// we can try this, traverse from left to right, the first number down is the wrong;
	// traverse from right to left, the first number up is the wrong
	// then exchange them, will recover the tree
	// 1. inorder traverse tree
	inorders := []*TreeNode{}
	nodes := []*TreeNode{}
	for root != nil || len(nodes) > 0 {
		if root != nil {
			nodes = append(nodes, root)
			root = root.Left
		} else {
			root = nodes[len(nodes)-1]
			nodes = nodes[:len(nodes)-1]
			inorders = append(inorders, root)
			root = root.Right
		}
	}
	// 2. traverse the list
	var left, right *TreeNode
	for i := 1; i < len(inorders); i++ {
		if inorders[i-1].Val > inorders[i].Val {
			left = inorders[i-1]
			break
		}
	}
	for i := len(inorders) - 2; i > -1; i-- {
		if inorders[i+1].Val < inorders[i].Val {
			right = inorders[i+1]
			break
		}
	}
	// 3. exchange the value
	left.Val, right.Val = right.Val, left.Val
}

func main() {
	n1 := &TreeNode{1, nil, nil}
	n2 := &TreeNode{2, nil, nil}
	n3 := &TreeNode{3, nil, nil}
	n1.Left = n3
	n3.Right = n2
	recoverTree(n1)
}
