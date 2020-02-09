#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if not nums:
            return None
        root_index = len(nums) // 2
        val = nums[root_index]
        root = TreeNode(val)
        # 左子树
        root.left = self.sortedArrayToBST(nums[:root_index]) if nums[:root_index] else None
        # 右子树
        root.right = self.sortedArrayToBST(nums[root_index+1:]) if nums[root_index+1:] else None
        return root

    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        nodes = [root]
        while nodes:
            level_result = []
            temp = []
            # 输出本层节点 并添加下一层的节点
            for node in nodes:
                level_result.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            result.append(level_result)
            nodes = temp[:]
        return result


def main():
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    root = solution.sortedArrayToBST(nums=nums)
    result = solution.levelOrderBottom(root=root)
    print(result)

if __name__ == "__main__":
    main()
