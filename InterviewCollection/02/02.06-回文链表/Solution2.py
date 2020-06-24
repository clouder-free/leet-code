#! /usr/bin/python

class ListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):

	def isPalindrome(self, head: ListNode) -> bool:
		if not head or not head.next:
			return True
		q, p = head, head.next
		# 两个节点
		if not p.next:
			return q.val == p.val
		while p:
			p = p.next
			if p:
				p = p.next
				q = q.next
		h = q
		q = q.next
		h.next = None
		while q:
			t = q.next
			q.next = h
			h, q = q, t

		while head:
			if head.val != h.val:
				return False
			head = head.next
			h = h.next

		if not h or not h.next:
			return True
		else:
			return False

def main():
	head = ListNode(1)
	n1 = ListNode(2)
	# n2 = ListNode(2)
	# n3 = ListNode(1)
	head.next = n1
	# n1.next = n2
	# n2.next = n3
	solution = Solution()
	result = solution.isPalindrome(head=head)
	print(result)

if __name__ == "__main__":
	main()


