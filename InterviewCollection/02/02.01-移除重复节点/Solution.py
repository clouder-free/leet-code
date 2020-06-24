#! /usr/bin/python

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

	def removeDuplicateNodes(self, head: ListNode) -> ListNode:
		if not head:
			return head
		p = head
		elements = set()
		elements.add(p.val)
		while p.next:
			if p.next.val in elements:
				p.next = p.next.next
			else:
				elements.add(p.next.val)
				p = p.next
		return head

def printListNode(head):
	while head:
		print(head.val, end=" ")
		head = head.next
	print()

def main():
	head = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(3)
	n5 = ListNode(2)
	n6 = ListNode(1)
	head.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	printListNode(head)
	solution = Solution()
	result = solution.removeDuplicateNodes(head=head)
	printListNode(result)

if __name__ == "__main__":
	main()
