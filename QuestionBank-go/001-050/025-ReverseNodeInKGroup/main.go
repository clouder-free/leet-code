package main

/*
K个一组翻转链表
*/

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	if k == 1 {
		return head
	}
	h := &ListNode{0, head}
	p := h
	for p != nil {
		n := p
		for i := 0; i < k; i += 1 {
			if n.Next != nil {
				n = n.Next
			} else {
				// 剩余长度不够K
				return h.Next
			}
		}
		m := p.Next
		// 逆序m到n之间的节点
		m, n = reverse(m, n)
		p.Next = m
		p = n
	}
	return h.Next
}

func reverse(head, tail *ListNode) (*ListNode, *ListNode) {
	h := &ListNode{0, nil}
	p := head
	for p != tail {
		q := p.Next
		p.Next = h.Next
		h.Next = p
		p = q
	}
	head.Next = tail.Next
	tail.Next = h.Next
	h.Next = tail
	return h.Next, head
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
	h5 := &ListNode{5, nil}
	h4 := &ListNode{4, h5}
	h3 := &ListNode{3, h4}
	h2 := &ListNode{2, h3}
	h1 := &ListNode{1, h2}
	printListNode(h1)
	result := reverseKGroup(h1, 4)
	printListNode(result)
}
