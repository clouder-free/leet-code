#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，返回它的前序遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,2,3]
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def preorderTraversal(self, root: TreeNode) -> [int]:
        results = []
        nodes = []
        while root or nodes:
            if root:
                results.append(root.val)
                nodes.append(root)
                root = root.left
            else:
                root = nodes.pop()
                root = root.right
        return results

    def preorderTraversal2(self, root: TreeNode) -> [int]:
        if root:
            return [root.val] + self.preorderTraversal2(root.left) + self.preorderTraversal2(root.right)
        return []


def main():
    root = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    root.left = t2
    root.right = t3
    t2.left = t4
    t4.right = t5
    t3.left = t6
    t6.left = t7
    solution = Solution()
    result = solution.preorderTraversal(root=root)
    print(result)

if __name__ == "__main__":
    main()