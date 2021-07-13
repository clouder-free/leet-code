# -*- coding: utf-8 -*-
"""
把二叉树转换为累加树
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        # 中序遍历 添加到list中 然后逐个累加即可
        def _inorder_traverse(node):
            if not node:
                return []
            return _inorder_traverse(node.left) + [node] + _inorder_traverse(node.right)
        nodes = _inorder_traverse(root)
        # 从后向前累加
        for i in range(len(nodes)-2, -1, -1):
            nodes[i].val += nodes[i+1].val
        values = [node.val for node in nodes]
        print(values)
        return root


def main():
    root = TreeNode(4)
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    root.left = n1
    root.right = n6
    n1.left = n0
    n1.right = n2
    n2.right = n3
    n6.left = n5
    n6.right = n7
    n7.right = n8
    result = Solution().convertBST(root)
    print(result.val)

if __name__ == '__main__':
    main()
