package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// merge sort list
func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	var pre *ListNode
	p, q := head, head
	for q != nil && q.Next != nil {
		pre = p
		p = p.Next
		q = q.Next.Next
	}
	n1 := sortList(pre.Next)
	pre.Next = nil
	n2 := sortList(head)
	return mergeNodes(n1, n2)
}

func mergeNodes(n1, n2 *ListNode) *ListNode {
	head := &ListNode{0, nil}
	p := head
	for n1 != nil || n2 != nil {
		if n1 == nil {
			p.Next = n2
			n2 = n2.Next
		} else if n2 == nil {
			p.Next = n1
			n1 = n1.Next
		} else if n1.Val < n2.Val {
			p.Next = n1
			n1 = n1.Next
		} else {
			p.Next = n2
			n2 = n2.Next
		}
		p = p.Next
	}
	return head.Next
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
	res := sortList(n1)
	printListNodes(res)
}
