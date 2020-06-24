#! /usr/bin/python

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def isBalanced(self, root: TreeNode) -> bool:
		def tree_height(node):
			if not node:
				return 0
			left = tree_height(node.left)
			right = tree_height(node.right)
			if left < 0 or right < 0 or abs(left-right) > 1:
				return -1
			return max(left, right) + 1
		return True if tree_height(root) >= 0 else False

def main():
	root = TreeNode(1)

if __name__ == "__main__":
	main()
