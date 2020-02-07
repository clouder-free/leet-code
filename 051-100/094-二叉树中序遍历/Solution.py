#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，返回它的中序遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def inorderTraversal(self, root: TreeNode) -> [int]:
        result = []
        def traverse(node):
            nodes = []
            while node or nodes:
                if node:
                    nodes.append(node)
                    node = node.left
                else:
                    node = nodes.pop()
                    result.append(node.val)
                    node = node.right
        traverse(root)
        return result

    def inorderTraversal2(self, root: TreeNode) -> [int]:
        result = []
        def inorder(root):
            if root:
                result.append(root.val)
                inorder(root.left)
                inorder(root.right)
        inorder(root)
        return result

def printLinkList(node):

    print(node.val, end="")
    while node.next:
        print("->", end="")
        node = node.next
        print(node.val, end="")
    print("")

def main():
    root = TreeNode(1)
    solution = Solution()
    result = solution.inorderTraversal(root=root)
    printLinkList(result)

if __name__ == "__main__":
    main()
