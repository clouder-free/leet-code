package main

/*
两两交换链表中的节点
*/

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	h := &ListNode{0, head}
	p := h
	for p.Next != nil && p.Next.Next != nil {
		m, n := p.Next, p.Next.Next
		p.Next, m.Next = n, n.Next
		n.Next = m
		p = m
	}
	return h.Next
}

func printListNode(head *ListNode) {
	for head != nil {
		print(head.Val)
		head = head.Next
		if head != nil {
			print("->")
		} else {
			println()
		}
	}
}

func main() {
	// h4 := &ListNode{4, nil}
	// h3 := &ListNode{3, nil}
	h2 := &ListNode{2, nil}
	h1 := &ListNode{1, h2}
	result := swapPairs(h1)
	printListNode(result)
}
