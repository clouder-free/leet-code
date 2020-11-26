# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

def printTreeNodeLevel(root):
    stack = [root]
    while stack:
        t = []
        for s in stack:
            print(s.val, end='')
            if s.left:
                t.append(s.left)
            if s.right:
                t.append(s.right)
        stack = t[:]
        print('')


if __name__ == '__main__':
    root = TreeNode(4)
    n2 = TreeNode(2)
    n7 = TreeNode(7)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n9 = TreeNode(9)
    root.left = n2
    root.right = n7
    n2.left = n1
    n2.right = n3
    n7.left = n6
    n7.right = n9
    printTreeNodeLevel(root=root)
    solution = Solution()
    root = solution.invertTree(root=root)
    printTreeNodeLevel(root)

