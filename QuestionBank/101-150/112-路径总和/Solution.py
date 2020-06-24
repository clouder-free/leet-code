#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
示例: 
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def path_sum(root, current):
            # 判断是否是叶节点
            if not root.left and not root.right:
                if current == sum:
                    return True
            # 不是叶节点
            else:
                if root.left and path_sum(root.left, current + root.left.val):
                    return True
                if root.right and path_sum(root.right, current + root.right.val):
                    return True
            return False
        return path_sum(root, root.val)

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
    root.left = t1
    root.right = t2
    t1.left = t3
    t3.left = t6
    t3.right = t7
    t2.left = t4
    t2.right = t5
    t5.right = t8
    sum = 22
    solution = Solution()
    result = solution.hasPathSum(root=root, sum=sum)
    print(result)

if __name__ == "__main__":
    main()
