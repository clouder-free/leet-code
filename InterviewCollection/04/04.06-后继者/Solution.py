#! /usr/bin/python

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
		results = []
		nodes = []
		while nodes or root:
			if root:
				nodes.append(root)
				root = root.left
			else:
				root = nodes.pop()
				results.append(root)
				if len(results) > 1 and results[-2].val == p.val:
					return results[-1]
				root = root.right
		return None

def main():
	root = TreeNode(5)
	n3 = TreeNode(3)
	n6 = TreeNode(6)
	n2 = TreeNode(2)
	n4 = TreeNode(4)
	n1 = TreeNode(1)
	root.left = n3
	root.right = n6
	n3.left = n2
	n3.right = n4
	n2.left = n1
	p = TreeNode(6)
	solution = Solution()
	result = solution.inorderSuccessor(root=root, p=p)
	if result:
		print("result:", result.val)
	else:
		print("None")

if __name__ == "__main__":
	main()
