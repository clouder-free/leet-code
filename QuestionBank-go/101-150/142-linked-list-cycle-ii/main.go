package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}
	slow, fast := head, head
	for slow != nil && slow.Next != nil {
		slow = slow.Next.Next
		fast = fast.Next
		if slow == fast {
			break
		}
	}
	if slow == fast {
		slow = head
		for slow != fast {
			slow = slow.Next
			fast = fast.Next
		}
		return slow
	}
	return nil
}
