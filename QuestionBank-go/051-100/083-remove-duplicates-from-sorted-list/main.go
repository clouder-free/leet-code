package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	// 判空
	if head == nil || head.Next == nil {
		return head
	}
	p, q := head, head
	for q != nil {
		if p.Val == q.Val {
			q = q.Next
		} else {
			p.Next = q
			p = q
		}
	}
	p.Next = q
	return head
}

func printLinkList(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val)
		if head.Next != nil {
			fmt.Print("->")
		}
		head = head.Next
	}
	fmt.Println()
}

func main() {
	// n51 := &ListNode{5, nil}
	// n5 := &ListNode{5, n51}
	// n42 := &ListNode{4, n5}
	// n41 := &ListNode{4, n42}
	n32 := &ListNode{3, nil}
	n31 := &ListNode{3, n32}
	// n2 := &ListNode{2, n31}
	n21 := &ListNode{2, n31}
	n1 := &ListNode{1, n21}
	head := &ListNode{1, n1}
	printLinkList(head)
	result := deleteDuplicates(head)
	printLinkList(result)

}
