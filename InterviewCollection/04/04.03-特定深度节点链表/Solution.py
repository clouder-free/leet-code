#! /usr/bin/python

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class ListNode(object):

	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):

	def listOfDepth(self, tree: TreeNode) -> [ListNode]:
		if not tree:
			return []
		result = []
		nodes = [tree]
		while nodes:
			res = []
			head, p = None, None
			for node in nodes:
				if node.left:
					res.append(node.left)
				if node.right:
					res.append(node.right)

				h = ListNode(node.val)
				if not head:
					head, p = h, h
				else:
					p.next, p = h, h
			result.append(head)
			nodes = res[:]
		return result

def printListNode(head):
	while head:
		print(head.val, end=" ")
		head = head.next
	print()

def main():
	root = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)
	n5 = TreeNode(5)
	n7 = TreeNode(7)
	n8 = TreeNode(8)
	root.left = n2
	root.right = n3
	n2.left = n4
	n2.right = n5
	n3.right = n7
	n4.left = n8
	solution = Solution()
	results = solution.listOfDepth(tree=root)
	for result in results:
		printListNode(result)

if __name__ == "__main__":
	main()

