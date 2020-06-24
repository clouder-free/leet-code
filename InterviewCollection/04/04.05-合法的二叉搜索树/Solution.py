#! /usr/bin/python

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def isValidBST(self, root: TreeNode) -> bool:
		nodes = []
		last = None
		while nodes or root:
			if root:
				nodes.append(root)
				root = root.left
			else:
				root = nodes.pop()
				if not last or last.val < root.val:
					last = root
				else:
					return False
				root = root.right
		return True

def main():
	root = TreeNode(5)
	n1 = TreeNode(1)
	n4 = TreeNode(4)
	n3 = TreeNode(3)
	n6 = TreeNode(6)
	root.left = n1
	root.right = n4
	n4.left = n3
	n4.right = n6
	solution = Solution()
	result = solution.isValidBST(root)
	print(result)

if __name__ == "__main__":
	main()
