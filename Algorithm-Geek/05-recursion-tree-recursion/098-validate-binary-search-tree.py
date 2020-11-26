# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            if not dfs(node.left, min_val, node.val):
                return False
            if not dfs(node.right, node.val, max_val):
                return False
            return True

        return dfs(root, float('-inf'), float('inf'))


def main():
    root = TreeNode()
    solution = Solution()
    result = solution.isValidBST(root=root)
    print(result)


if __name__ == '__main__':
    main()



