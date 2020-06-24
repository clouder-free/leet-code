#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。
示例:
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度2.
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def minDepth(self, root: TreeNode) -> int:
        # 层次遍历
        if not root:
            return 0
        nodes = [root]
        depth = 1
        while nodes:
            temp = []
            for node in nodes:
                # 判断有没有叶子节点
                if not node.left and not node.right:
                    return depth
                else:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            nodes = temp[:]
            depth += 1
        return 0

def main():
    root = TreeNode(3)
    t1 = TreeNode(9)
    t2 = TreeNode(20)
    t3 = TreeNode(15)
    t4 = TreeNode(7)
    root.left = t1
    root.right = t2
    t2.left = t3
    t2.right = t4
    solution = Solution()
    result = solution.minDepth(root=root)
    print(result)

if __name__ == "__main__":
    main()
