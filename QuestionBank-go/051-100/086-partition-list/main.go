package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	fakeHead := &ListNode{0, head}
	upperHead := &ListNode{0, nil}
	p, q := fakeHead, upperHead

	for head != nil {
		if head.Val < x {
			p.Next = head
			// move forward p and head
			p = p.Next
			head = head.Next
			// cut the link
			p.Next = nil
		} else {
			q.Next = head
			// move forward q and head
			q = q.Next
			head = head.Next
			q.Next = nil
		}
	}
	// link p(lower) and q(upper)
	p.Next = upperHead.Next
	return fakeHead.Next
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
	n5 := &ListNode{2, nil}
	n4 := &ListNode{5, n5}
	n3 := &ListNode{2, n4}
	n2 := &ListNode{3, n3}
	n1 := &ListNode{4, n2}
	head := &ListNode{1, n1}
	printLinkList(head)
	result := partition(head, 3)
	printLinkList(result)

}
