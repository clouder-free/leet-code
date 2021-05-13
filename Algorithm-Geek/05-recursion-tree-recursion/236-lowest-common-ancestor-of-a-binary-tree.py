# -*- coding: utf-8 -*-


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return left if left else right


if __name__ == '__main__':
    root = TreeNode(1)
    solution = Solution()
    ancs = solution.lowestCommonAncestor(root=root, p=None, q=None)


