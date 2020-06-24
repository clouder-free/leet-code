#! /usr/bin/python

class ListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):

	def isPalindrome(self, head: ListNode) -> bool:
		if not head:
			return True
		p = head
		values = []
		while p:
			values.append(p.val)
			p = p.next
		i, j = 0, len(values) - 1
		while i <= j:
			if values[i] == values[j]:
				i += 1
				j -= 1
			else:
				return False
		return True

def main():
	head = ListNode(1)
	n1 = ListNode(2)
	n2 = ListNode(2)
	n3 = ListNode(1)
	head.next = n1
	n1.next = n2
	n2.next = n3
	solution = Solution()
	result = solution.isPalindrome(head=head)
	print(result)

if __name__ == "__main__":
	main()


