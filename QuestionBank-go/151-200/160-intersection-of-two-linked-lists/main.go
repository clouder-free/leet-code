package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	nodes := make(map[*ListNode]bool)
	for headA != nil || headB != nil {
		if headA != nil {
			if nodes[headA] {
				return headA
			} else {
				nodes[headA] = true
				headA = headA.Next
			}
		}
		if headB != nil {
			if nodes[headB] {
				return headB
			} else {
				nodes[headB] = true
				headB = headB.Next
			}
		}
	}
	return nil
}
