package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type BSTIterator struct {
	Nodes []int
	Index int
}

func Constructor(root *TreeNode) BSTIterator {
	// construct
	bst := &BSTIterator{Nodes: []int{}, Index: -1}
	// init
	inorder(root, bst)
	return *bst
}

func inorder(root *TreeNode, bst *BSTIterator) {
	if root == nil {
		return
	}
	inorder(root.Left, bst)
	bst.Nodes = append(bst.Nodes, root.Val)
	inorder(root.Right, bst)
}

func (this *BSTIterator) Next() int {
	this.Index++
	return this.Nodes[this.Index]
}

func (this *BSTIterator) HasNext() bool {
	return this.Index < len(this.Nodes)-1
}

func main() {

}
