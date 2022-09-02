package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return []*TreeNode{nil}
	}
	return createTrees(1, n)
}

func createTrees(start, end int) []*TreeNode {
	trees := []*TreeNode{}
	if start > end {
		trees = append(trees, nil)
		return trees
	}
	for i := start; i <= end; i++ {
		// left tree
		lefts := createTrees(start, i-1)
		// right tree
		rights := createTrees(i+1, end)
		// generate
		for m := 0; m < len(lefts); m++ {
			for n := 0; n < len(rights); n++ {
				root := &TreeNode{i, lefts[m], rights[n]}
				trees = append(trees, root)
			}
		}
	}
	return trees
}

func main() {
	result := generateTrees(3)
	fmt.Println("result:", result)
}
