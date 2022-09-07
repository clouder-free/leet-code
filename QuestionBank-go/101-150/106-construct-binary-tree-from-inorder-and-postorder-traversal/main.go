package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(inorder) == 0 || len(postorder) == 0 {
		return nil
	}
	root := &TreeNode{postorder[len(postorder)-1], nil, nil}
	if len(inorder) == 1 || len(postorder) == 1 {
		return root
	}
	// root index inorder
	var index int
	for i := 0; i < len(inorder); i++ {
		if inorder[i] == root.Val {
			index = i
			break
		}
	}
	// left tree inorder traversal inorder[:i]
	// left tree postorder traversal postorder[:i]
	// right tree inorder traversal inorder[i+1:]
	// right tree postorder traversal postorder[i+1:len(postorder)-1]
	root.Left = buildTree(inorder[:index], postorder[:index])
	root.Right = buildTree(inorder[index+1:], postorder[index:len(postorder)-1])
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
	inorder := []int{9, 3, 15, 20, 7}
	postorder := []int{9, 15, 7, 20, 3}
	result := buildTree(inorder, postorder)
	printTree(result)
}
