#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，返回其节点值自底向上的层次遍历。
(即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        nodes = [root]
        while nodes:
            level_result = []
            temp = []
            # 输出本层节点 并添加下一层的节点
            for node in nodes:
                level_result.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            result = [level_result] + result
            nodes = temp[:]
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
    result = solution.levelOrderBottom(root=root)
    print(result)

if __name__ == "__main__":
    main()

