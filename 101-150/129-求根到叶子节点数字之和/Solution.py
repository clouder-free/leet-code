#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，它的每个结点都存放一个0-9的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。
示例 1:
输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:
输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        def sum_numbers(root, value):
            if not root.left and not root.right:
                result.append(value*10 + root.val)
                return
            if root.left:
                sum_numbers(root.left, value*10 + root.val)
            if root.right:
                sum_numbers(root.right, value*10 + root.val)
        sum_numbers(root, 0)
        return sum(result)

def main():
    root = TreeNode(4)
    t1 = TreeNode(9)
    t2 = TreeNode(0)
    t3 = TreeNode(5)
    t4 = TreeNode(1)
    root.left = t1
    root.right = t2
    t1.left = t3
    t1.right = t4
    solution = Solution()
    result = solution.sumNumbers(root=root)
    print(result)

if __name__ == "__main__":
    main()
