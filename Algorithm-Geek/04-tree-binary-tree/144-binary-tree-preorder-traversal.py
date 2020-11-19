# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def preorderTraversal(self, root: TreeNode) -> [int]:
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        return []

    def preorderTraversal2(self, root: TreeNode) -> [int]:
        result = []
        stack = []
        while root or stack:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return result


def main():
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    root = TreeNode(val=1, left=n2, right=n3)
    n2.right = n4
    n3.left = n5
    solution = Solution()
    result = solution.preorderTraversal2(root=root)
    print(result)

if __name__ == '__main__':
    main()



