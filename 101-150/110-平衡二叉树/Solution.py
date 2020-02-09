#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isBalanced(self, root: TreeNode) -> bool:
        def balanced(root):
            if not root:
                return 0
            left = balanced(root.left)
            if left == -1:
                return -1
            right = balanced(root.right)
            if right == -1:
                return -1
            return max([left, right])+1 if abs(left-right) < 2 else -1
        return balanced(root) != -1

    def isBalanced2(self, root: TreeNode) -> bool:
        def tree_height(root):
            if not root:
                return 0
            left = tree_height(root.left)
            right = tree_height(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return max([left, right]) + 1
        return True if tree_height(root) >= 0 else False

def main():
    root = TreeNode(1)
    solution = Solution()
    result = solution.isBalanced(root=root)
    print(result)

if __name__ == "__main__":
    main()
