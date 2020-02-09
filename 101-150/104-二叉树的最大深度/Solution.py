#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3。
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # BFS 广度优先遍历
        deep = 0
        nodes = [root]
        while nodes:
            deep += 1
            temp = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            nodes = temp[:]
        return deep

    def maxDepth2(self, root: TreeNode) -> int:
        def depth(node, deep):
            if not node:
                return deep
            left = depth(node.left, deep+1) if node.left else deep
            right = depth(node.right, deep+1) if node.right else deep
            return left if left > right else right
        return depth(root, 1) if root else 0

def main():
    root = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(2)
    l4 = TreeNode(3)
    l5 = TreeNode(4)
    l6 = TreeNode(4)
    l7 = TreeNode(3)
    root.left = l2
    root.right = l3
    l2.left = l4
    l2.right = l5
    l3.left = l6
    l3.right = l7
    solution = Solution()
    result = solution.maxDepth(root=root)
    print(result)

if __name__ == "__main__":
    main()



