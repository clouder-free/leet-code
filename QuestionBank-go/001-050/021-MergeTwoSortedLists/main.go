package main

/*
合并两个有序链表
*/

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	head := &ListNode{0, nil}
	p := head
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			p.Next = list1
			list1 = list1.Next
		} else {
			p.Next = list2
			list2 = list2.Next
		}
		p = p.Next
	}
	if list1 != nil {
		p.Next = list1
	}
	if list2 != nil {
		p.Next = list2
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
	l1 := &ListNode{4, nil}
	l2 := &ListNode{2, l1}
	l3 := &ListNode{1, l2}
	printListNode(l3)
	h1 := &ListNode{4, nil}
	h2 := &ListNode{3, h1}
	h3 := &ListNode{1, h2}
	printListNode(h3)
	h := mergeTwoLists(l3, h3)
	printListNode(h)
}
