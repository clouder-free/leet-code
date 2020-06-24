#! /usr/bin/python

class ListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):

	def detectCycle(self, head: ListNode) -> ListNode:
		if not head:
			return None
		nodes = set()
		p = head
		while p:
			if p in nodes:
				return p
			nodes.add(p)
			p = p.next
		return None

def printListNode(head):
	while head:
		print(head.val, end=" ")
		head = head.next
	print()

def main():
	head = ListNode(3)
	n1 = ListNode(2)
	n2 = ListNode(0)
	n3 = ListNode(-4)
	head.next = n1
	n1.next = n2
	n2.next = n3
	n3.next = n1
	solution = Solution()
	result = solution.detectCycle(head=head)
	if result:
		print(result.val)
	else:
		print("None")

if __name__ == "__main__":
	main()
