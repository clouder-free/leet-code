package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (node *ListNode) PrintNodeValue() {
	for node != nil {
		fmt.Printf("%d ", node.Val)
		node = node.Next
	}
	fmt.Println()
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var head, tail *ListNode
	var v int
	for l1 != nil || l2 != nil {
		var v1, v2 int
		if l1 != nil {
			v1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			v2 = l2.Val
			l2 = l2.Next
		}
		val := (v + v1 + v2) % 10
		v = (v + v1 + v2) / 10
		node := ListNode{val, nil}
		if head != nil {
			tail.Next = &node
			tail = tail.Next
		} else {
			head = &node
			tail = head
		}
	}
	if v != 0 {
		node := ListNode{v, nil}
		tail.Next = &node
		tail = tail.Next
	}
	return head
}

func main() {
	l1 := ListNode{2, nil}
	n1 := ListNode{4, nil}
	n2 := ListNode{3, nil}
	l1.Next = &n1
	n1.Next = &n2

	l2 := ListNode{5, nil}
	n3 := ListNode{6, nil}
	n4 := ListNode{4, nil}
	l2.Next = &n3
	n3.Next = &n4

	l1.PrintNodeValue()
	l2.PrintNodeValue()
	node := addTwoNumbers(&l1, &l2)
	node.PrintNodeValue()
}
