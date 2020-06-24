#! /usr/bin/python

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

	def kthToLast(self, head: ListNode, k: int) -> int:
		p, q = head, head
		while k > 1:
			p = p.next
			k -= 1
		while p.next:
			p = p.next
			q = q.next
		return q.val

def main():
	head = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)
	head.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	k = 2
	solution = Solution()
	result = solution.kthToLast(head=head, k=k)
	print(result)

if __name__ == "__main__":
	main()
