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
        if not root:
            return []
        result = []
        stack = [root]
        stack2 = []
        while stack:
            node = stack.pop()
            stack2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while stack2:
            result.append(stack2.pop().val)
        return result

    def postorderTraversal2(self, root: TreeNode) -> [int]:
        if root:
            return self.postorderTraversal2(root.left) + self.postorderTraversal2(root.right) + [root.val]
        return []

def main():
    root = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    root.left = t2
    root.right = t3
    t2.left = t4
    t4.right = t5
    t3.left = t6
    t6.left = t7
    solution = Solution()
    result = solution.postorderTraversal(root=None)
    print(result)

if __name__ == "__main__":
    main()