#! /usr/bin/python

class ListNode(object):

	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):

	def partition(self, head: ListNode, x: int) -> ListNode:
		if not head:
			return head
		left, right = None, None
		p, q = None, None
		cur = head
		while cur:
			# 左侧
			if cur.val < x:
				if left:
					p.next = cur
					p = p.next
				else:
					left, p = cur, cur
			# 右侧
			else:
				if right:
					q.next = cur
					q = q.next
				else:
					right, q = cur, cur
			cur = cur.next
		if left:
			p.next = right
		if right:
			q.next = None
		return left if left else right

def printLinkNode(head):
	while head:
		print(head.val, end=" ")
		head = head.next
	print("")

def main():
	head = ListNode(2)
	n1 = ListNode(1)
	# n2 = ListNode(5)
	# n3 = ListNode(8)
	# n4 = ListNode(5)
	# n5 = ListNode(10)
	# n6 = ListNode(2)
	# n7 = ListNode(1)
	head.next = n1
	# n2.next = n3
	# n3.next = n4
	# n4.next = n5
	# n5.next = n6
	# n6.next = n7
	printLinkNode(head)
	solution = Solution()
	result = solution.partition(head=head, x=2)
	printLinkNode(result)

if __name__ == "__main__":
	main()
