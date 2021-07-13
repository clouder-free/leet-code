# -*- coding: utf-8 -*-
"""
二叉树的直径
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 1
        def _dfs(root):
            if not root:
                return 0
            # 左子树为根的子树的深度
            l = _dfs(root.left)
            # 右子树为根的子树的深度
            r = _dfs(root.right)
            self.result = max(self.result, l+r+1)
            return max(l, r) + 1
        _dfs(root)
        return self.result - 1


def main():
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.left = n2
    root.right = n3
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2.left = n4
    n2.right = n5
    print(Solution().diameterOfBinaryTree(root))


if __name__ == '__main__':
    main()
