#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
输入:
    2
   / \
  1   3
输出: true
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历 为有序数组
        roots = []
        last = None
        while root or roots:
            if root:
                roots.append(root)
                root = root.left
            else:
                root = roots.pop()
                if not last:
                    last = root
                elif last.val >= root.val:
                    return False
                else:
                    last = root
                root = root.right
        return True

def main():
    root = TreeNode(10)
    l1 = TreeNode(5)
    l2 = TreeNode(15)
    l3 = TreeNode(6)
    l4 = TreeNode(20)
    root.left = l1
    root.right = l2
    l2.left = l3
    l2.right = l4
    solution = Solution()
    result = solution.isValidBST(root=root)
    print(result)

if __name__ == "__main__":
    main()


