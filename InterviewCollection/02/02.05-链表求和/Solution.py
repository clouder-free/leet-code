#! /usr/bin/python

class ListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):

	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		if not l1 and not l2:
			return None
		if not l1 or not l2:
			return l1 if l1 else l2
		head, cur = l1, None
		k = 0
		while l1 and l2:
			cur = l1
			s = k + l1.val + l2.val
			l1.val = s % 10
			k = s // 10
			l1 = l1.next
			l2 = l2.next
		if l1 or l2:
			if l2:
				cur.next = l2
			cur = cur.next
			while cur:
				t = k + cur.val
				cur.val = t % 10
				k = t // 10
				if not cur.next:
					break
				cur = cur.next
		# 最后一位是否进位:
		if k != 0:
			cur.next = ListNode(k)
		return head

	# 新建节点
	def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
		if not l1 and not l2:
			return None
		if not l1 or not l2:
			return l1 if l1 else l2
		head, p = None, None
		k = 0
		while l1 or l2:
			val1 = l1.val if l1 else 0
			val2 = l2.val if l2 else 0
			t = k + val1 + val2
			val = t % 10
			k = t // 10
			if head:
				p.next = ListNode(val)
				p = p.next
			else:
				head = ListNode(val)
				p = head
			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next
		if k != 0:
			p.next = ListNode(k)
		return head

def printLinkNode(head):
	while head:
		print(head.val, end=" ")
		head = head.next
	print()

def main():
	h1 = ListNode(9)
	n1 = ListNode(8)
	h1.next = n1
	# n2 = ListNode(6)
	# h1.next = n1
	# n1.next = n2
	printLinkNode(h1)
	h2 = ListNode(1)
	# n3 = ListNode(8)
	# n4 = ListNode(3)
	# h2.next = n3
	# n3.next = n4
	printLinkNode(h2)
	solution = Solution()
	result = solution.addTwoNumbers2(l1=h1, l2=h2)
	printLinkNode(result)

if __name__ == "__main__":
	main()
