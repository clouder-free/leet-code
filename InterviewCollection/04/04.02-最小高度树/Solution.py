#! /usr/bin/python

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def sortedArrayToBST(self, nums: [int]) -> TreeNode:
		if not nums:
			return None
		i = len(nums) // 2
		root = TreeNode(nums[i])
		root.left = self.sortedArrayToBST(nums=nums[:i])
		root.right = self.sortedArrayToBST(nums=nums[i+1:])
		return root

def main():
	solution = Solution()

if __name__ == "__main__":
	main()
