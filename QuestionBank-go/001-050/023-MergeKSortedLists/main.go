package main

/*
合并K个升序链表
*/

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}
	if len(lists) == 1 {
		return lists[0]
	}
	mid := len(lists) / 2
	// 左半部分 右半部分
	left := mergeKLists(lists[:mid])
	right := mergeKLists(lists[mid:])
	// 合并左半 右半
	head := &ListNode{0, nil}
	p := head
	for left != nil && right != nil {
		if left.Val <= right.Val {
			p.Next = left
			left = left.Next
		} else {
			p.Next = right
			right = right.Next
		}
		p = p.Next
	}
	if left != nil {
		p.Next = left
	}
	if right != nil {
		p.Next = right
	}
	return head.Next
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
	h1 := &ListNode{5, nil}
	h2 := &ListNode{4, h1}
	h3 := &ListNode{1, h2}
	l1 := &ListNode{4, nil}
	l2 := &ListNode{3, l1}
	l3 := &ListNode{1, l2}
	m1 := &ListNode{6, nil}
	m2 := &ListNode{2, m1}
	result := mergeKLists([]*ListNode{h3, l3, m2})
	h := mergeKLists([]*ListNode{})
	printListNode(result)
	printListNode(h)
}
