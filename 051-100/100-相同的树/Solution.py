#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
示例 1:
输入:       1         1
          / \       / \
         2   3     2   3
        [1,2,3],   [1,2,3]
输出: true
示例 2:
输入:      1          1
          /           \
         2             2
        [1,2],     [1,null,2]
输出: false
示例 3:
输入:       1         1
          / \       / \
         2   1     1   2
        [1,2,1],   [1,1,2]
输出: false
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p q 都为空
        if not p and not q:
            return True
        # p q 有一个为空
        if (p and not q) or (not p and q):
            return False
        # p q 都不为空
        # 值不相等
        if p.val != q.val:
            return False
        # 左子树与右子树分别是否相同
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def main():
    p = TreeNode(1)
    p1 = TreeNode(2)
    p2 = TreeNode(1)
    p.left = p1
    p.right = p2
    q = TreeNode(1)
    q1 = TreeNode(1)
    q2 = TreeNode(2)
    q.left = q1
    q.right = q2
    solution = Solution()
    result = solution.isSameTree(p=p, q=q)
    print(result)

if __name__ == "__main__":
    main()

