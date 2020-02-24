#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
二叉搜索树中的两个节点被错误地交换。
请在不改变其结构的情况下，恢复这棵树。
示例 1:
输入: [1,3,null,null,2]
   1
  /
 3
  \
   2
输出: [3,1,null,null,2]
   3
  /
 1
  \
   2
示例 2:
输入: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
输出: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def recoverTree(self, root: TreeNode) -> None:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)
        roots = inorder(root)
        first, second = None, None
        for i in range(1, len(roots)):
            if roots[i-1].val > roots[i].val:
                first = roots[i-1]
                break
        for i in range(len(roots)-2, -1, -1):
            if roots[i+1].val < roots[i].val:
                second = roots[i+1]
                break
        # 交换错误节点的值
        first.val, second.val = second.val, first.val

def main():
    root = TreeNode(3)
    solution = Solution()
    solution.recoverTree(root=root)

if __name__ == "__main__":
    main()



