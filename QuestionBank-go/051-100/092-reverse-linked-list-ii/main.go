package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	// head nil
	if head == nil || head.Next == nil {
		return head
	}
	// location index
	if left == right {
		return head
	}
	// init
	fakeHead := &ListNode{0, head}
	p := fakeHead
	i := 1
	for ; i < left; i++ {
		p = p.Next
	}
	phead, ptail := p.Next, p.Next
	// move
	for ; i < right; i++ {
		q := ptail
		ptail = ptail.Next
		q.Next = p.Next
		p.Next = q
	}
	// right location
	phead.Next = ptail.Next
	ptail.Next = p.Next
	p.Next = ptail
	// return
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
	n5 := &ListNode{5, nil}
	n4 := &ListNode{4, n5}
	n3 := &ListNode{3, n4}
	n2 := &ListNode{2, n3}
	n1 := &ListNode{1, n2}
	head := &ListNode{0, n1}
	printLinkList(head)
	result := reverseBetween(head, 3, 6)
	printLinkList(result)

}
