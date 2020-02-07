#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，返回它的后序遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def postorderTraversal(self, root: TreeNode) -> [int]:
        result = []
        if not root:
            return result
        def traverse(node):
            stack = [node]
            stack2 = []
            while stack:
                n = stack.pop()
                stack2.append(n)
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            while stack2:
                result.append(stack2.pop().val)
        traverse(node=root)
        return result

    def postorderTraversal2(self, root: TreeNode) -> [int]:
        result = []
        if not root:
            return result
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.val)
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
    result = solution.postorderTraversal(root=root)
    print(result)

if __name__ == "__main__":
    main()