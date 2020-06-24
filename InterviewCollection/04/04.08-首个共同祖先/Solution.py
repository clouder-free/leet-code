#! /usr/bin/python

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		if not root:
			return None
		if root.val in [p.val, q.val]:
			return root
		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)
		if left and right:
			return root
		elif left:
			return left
		elif right:
			return right
		return None

	def preorder(self, root: TreeNode) -> [int]:
		result = []
		nodes = []
		while nodes or root:
			if root:
				result.append(root.val)
				nodes.append(root)
				root = root.left
			else:
				root = nodes.pop()
				root = root.right
		return result

def main():
	root = TreeNode(3)
	n5 = TreeNode(5)
	n1 = TreeNode(1)
	n6 = TreeNode(6)
	n2 = TreeNode(2)
	n0 = TreeNode(0)
	n8 = TreeNode(8)
	n7 = TreeNode(7)
	n4 = TreeNode(4)
	root.left = n5
	root.right = n1
	n5.left = n6
	n5.right = n2
	n2.left = n7
	n2.right = n4
	n1.left = n0
	n1.right = n8
	solution = Solution()
	result = solution.preorder(root=root)
	print(result)

if __name__ == "__main__":
	main()
