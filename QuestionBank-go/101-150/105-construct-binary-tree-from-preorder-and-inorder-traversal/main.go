package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 || len(inorder) == 0 {
		return nil
	}
	root := &TreeNode{preorder[0], nil, nil}
	// only one node
	if len(preorder) == 1 || len(inorder) == 1 {
		return root
	}
	// root index of inorder
	var index int
	for i := 0; i < len(inorder); i++ {
		if inorder[i] == root.Val {
			index = i
			break
		}
	}
	// left child tree preorder--preorder[1:i+1]
	// left child tree inorder--inorder[:i]
	// right child tree preorder--preorder[i+1:]
	// right child tree inorder--inorder[i+1:]
	// construct left tree
	root.Left = buildTree(preorder[1:index+1], inorder[:index])
	root.Right = buildTree(preorder[index+1:], inorder[index+1:])
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
	preorder := []int{3, 9, 20, 15, 7}
	inorder := []int{9, 3, 15, 20, 7}
	result := buildTree(preorder, inorder)
	printTree(result)
}
