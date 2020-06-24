#! /usr/bin/python

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

	def BSTSequences(self, root: TreeNode) -> [[int]]:
		if not root:
			return []
		result = []
		nodes = [root]
		while nodes:
			res = []
			# 当前数组的全排列
			def all_sorts(nums, temp):
				if not nums:
					res.append(temp[:])
				for i in range(len(nums)):
					temp.append(nums[i])
					all_sorts(nums=nums[:i]+nums[i+1:], temp=temp)
					temp.pop()

			all_sorts(nums=[node.val for node in nodes], temp=[])
			print(res)
			# 添加到result中
			result = [r.extend(t) for r in result for t in res]
			# 下一行
			t = []
			for node in nodes:
				if node.left:
					t.append(node.left)
				if node.right:
					t.append(node.right)
			nodes = t[:]
		return result

def main():
	root = TreeNode(2)
	n1 = TreeNode(1)
	n3 = TreeNode(3)
	root.left = n1
	root.right = n3
	solution = Solution()
	result = solution.BSTSequences(root=root)
	print(result)

if __name__ == "__main__":
	main()