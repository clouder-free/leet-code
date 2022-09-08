package main

type ListNode struct {
	Val  int
	Next *ListNode
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedListToBST(head *ListNode) *TreeNode {
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return &TreeNode{head.Val, nil, nil}
	}
	last := head.Next
	mid := head
	var preMid *ListNode
	for last != nil {
		last = last.Next
		if last != nil {
			last = last.Next
			if preMid != nil {
				preMid = preMid.Next
			} else {
				preMid = mid
			}
			mid = mid.Next
		}
	}
	if preMid != nil {
		preMid.Next = nil
	}
	root := &TreeNode{mid.Val, nil, nil}
	// left tree
	if preMid != nil {
		root.Left = sortedListToBST(head)
	}
	if mid.Next != nil {
		root.Right = sortedListToBST(mid.Next)
	}
	return root
}

func main() {

}
