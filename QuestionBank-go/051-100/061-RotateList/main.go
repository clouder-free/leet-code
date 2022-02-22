package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || k == 0 {
		return head
	}
	// 确定链表长度
	tail, length := head, 1
	for tail.Next != nil {
		tail = tail.Next
		length++
	}
	// 确定K
	k %= length
	if k == 0 {
		return head
	}
	// 开始移动
	p, q := head, head
	for i := 1; p != tail; {
		p = p.Next
		i++
		if i > k+1 {
			q = q.Next
		}
	}
	// q.Next为新的head
	tail.Next, head = head, q.Next
	q.Next = nil
	return head
}

func printLinkNodes(head *ListNode) {
	for head != nil {
		fmt.Printf("%d", head.Val)
		if head.Next != nil {
			fmt.Print("->")
		}
		head = head.Next
	}
	fmt.Println()
}

func main() {
	n1 := &ListNode{0, nil}
	n2 := &ListNode{1, nil}
	n3 := &ListNode{2, nil}
	//n4 := &ListNode{4, nil}
	//n5 := &ListNode{5, nil}
	n1.Next = n2
	n2.Next = n3
	//n3.Next = n4
	//n4.Next = n5
	printLinkNodes(n1)
	head := rotateRight(n1, 4)
	printLinkNodes(head)
}
