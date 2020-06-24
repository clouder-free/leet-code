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
        result = []
        if not root:
            return result
        def traverse(node):
            nodes = [node]
            while nodes:
                result.append(node.val)
                if node.right:
                    nodes.append(node.right)
                if node.left:
                    nodes.append(node.left)
                node = nodes.pop()
        traverse(node=root)
        return result

    def preorderTraversal2(self, root: TreeNode) -> [int]:
        result = []
        if not root:
            return result
        def traverse(node):
            if node:
                result.append(node.val)
                traverse(node.left)
                traverse(node.right)
        traverse(node=root)
        return result

def main():
    root = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    root.left = l2
    root.right = l3
    l2.right = l4
    l3.left = l5
    solution = Solution()
    result = solution.preorderTraversal2(root=root)
    print(result)

if __name__ == "__main__":
    main()