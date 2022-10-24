package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	// use list to store all nodes
	nodes := []*ListNode{}
	for p := head; p != nil; p = p.Next {
		nodes = append(nodes, p)
	}
	// use list to store all nodes
	i, j := 0, len(nodes)-1
	for ; i < j; i, j = i+1, j-1 {
		nodes[i].Next, nodes[j].Next = nodes[j], nodes[i].Next
	}
	nodes[i].Next = nil
	printLinkList(head)
}

func printLinkList(head *ListNode) {
	for ; head != nil; head = head.Next {
		fmt.Printf("%v", head.Val)
		if head.Next != nil {
			fmt.Print("->")
		}
	}
	fmt.Println()
}

func main() {
	n5 := &ListNode{5, nil}
	n4 := &ListNode{4, n5}
	n3 := &ListNode{3, n4}
	n2 := &ListNode{2, n3}
	n1 := &ListNode{1, n2}
	printLinkList(n1)
	reorderList(n1)
}
