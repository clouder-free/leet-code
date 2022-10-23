package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	p := head
	for p != nil {
		p = p.Next
		if p == nil {
			return false
		}
		p = p.Next
		head = head.Next
		if p == head {
			return true
		}
	}
	return false
}
