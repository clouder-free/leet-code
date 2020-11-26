# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return left + 1 if left > right else right + 1

def main():
    root = TreeNode(1)
    solution = Solution()
    result = solution.maxDepth(root=root)
    print(result)

if __name__ == '__main__':
    main()




