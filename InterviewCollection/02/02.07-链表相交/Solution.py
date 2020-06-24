#! /usr/bin/python

class ListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):

	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		if not headA or not headB:
			return None
		nodes = set()
		p = headA
		while p:
			nodes.add(p)
			p = p.next
		p = headB
		while p:
			if p in nodes:
				return p
			p = p.next
		return None

def printListNode(head):
	while head:
		print(head.val, end=" ")
		head = head.next
	print()

def main():
	headA = ListNode(4)
	n1 = ListNode(1)
	n2 = ListNode(8)
	n3 = ListNode(4)
	n4 = ListNode(5)
	headA.next = n1
	n1.next = n2
	n2.next = n3
	n3.next = n4
	headB = ListNode(5)
	n5 = ListNode(0)
	n6 = ListNode(1)
	headB.next = n5
	n5.next = n6
	n6.next = n2
	printListNode(headA)
	printListNode(headB)
	solution = Solution()
	result = solution.getIntersectionNode(headA=headA, headB=headB)
	if result:
		print(result.val)
	else:
		print("None")

if __name__ == "__main__":
	main()

