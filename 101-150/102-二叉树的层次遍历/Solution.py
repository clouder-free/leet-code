#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def levelOrder(self, root: TreeNode) -> [[int]]:
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
            result.append(level_result)
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
    result = solution.levelOrder(root=root)
    print(result)

if __name__ == "__main__":
    main()

