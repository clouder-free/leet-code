# -*- coding: utf-8 -*-


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        pass


if __name__ == '__main__':
    root = TreeNode(1)
    solution = Solution()
    ancs = solution.lowestCommonAncestor(root=root, p=None, q=None)


