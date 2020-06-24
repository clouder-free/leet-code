#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def pathSum(self, root: TreeNode, target: int) -> [[int]]:
        if not root:
            return []
        result = []
        def path_sum(node, temp):
            print("temp:", temp)
            if not node.left and not node.right:
                if sum(temp) == target:
                    result.append(temp[:])
            else:
                if node.left:
                    path_sum(node.left, temp[:] + [node.left.val])
                if node.right:
                    path_sum(node.right, temp[:] + [node.right.val])
        temp = [root.val]
        path_sum(root, temp[:])
        return result

def main():
    root = TreeNode(5)
    t1 = TreeNode(4)
    t2 = TreeNode(8)
    t3 = TreeNode(11)
    t4 = TreeNode(13)
    t5 = TreeNode(4)
    t6 = TreeNode(7)
    t7 = TreeNode(2)
    t8 = TreeNode(1)
    t9 = TreeNode(5)
    root.left = t1
    root.right = t2
    t1.left = t3
    t3.left = t6
    t3.right = t7
    t2.left = t4
    t2.right = t5
    t5.left = t9
    t5.right = t8
    sum = 22
    solution = Solution()
    result = solution.pathSum(root=root, target=sum)
    print(result)

if __name__ == "__main__":
    main()

