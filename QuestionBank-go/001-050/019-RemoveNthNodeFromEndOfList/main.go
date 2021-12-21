package main

/*
删除链表的倒数第N个结点
*/
type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// 新增辅助节点
	h := &ListNode{0, head}
	p, q := h, h
	for i := 0; p.Next != nil; {
		p = p.Next
		if i >= n {
			q = q.Next
		}
		i += 1
	}
	q.Next = q.Next.Next
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
	h5 := &ListNode{5, nil}
	h4 := &ListNode{4, h5}
	h3 := &ListNode{3, h4}
	h2 := &ListNode{2, h3}
	h1 := &ListNode{1, h2}
	printListNode(h1)
	h := &ListNode{1, nil}
	printListNode(h4)
	h = removeNthFromEnd(h4, 2)
	printListNode(h)
}
