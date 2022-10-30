package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func insertionSortList(head *ListNode) *ListNode {
	p := head
	head = nil
	var tail *ListNode
	for p != nil {
		if head == nil {
			head, tail = p, p
			p = p.Next
			tail.Next = nil
		} else {
			q := p
			p = p.Next
			if q.Val <= head.Val {
				q.Next = head
				head = q
			} else if q.Val > head.Val && q.Val < tail.Val {
				k := head
				for k.Next.Val < q.Val {
					k = k.Next
				}
				q.Next, k.Next = k.Next, q
			} else {
				tail.Next = q
				tail = tail.Next
				tail.Next = nil
			}
		}
	}
	return head
}

func printListNodes(head *ListNode) {
	for ; head != nil; head = head.Next {
		fmt.Printf("%v", head.Val)
		if head.Next != nil {
			fmt.Printf("->")
		}
	}
	fmt.Println()
}

func main() {
	n3 := &ListNode{1, nil}
	n2 := &ListNode{2, n3}
	n1 := &ListNode{3, n2}
	printListNodes(n1)
	res := insertionSortList(n1)
	printListNodes(res)

}
