#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，原地将它展开为链表。
例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def flatten(self, root: TreeNode) -> None:
        while root:
            if root.left:
                # 找到左子树最右侧的点
                r = root.left
                while r.right:
                    r = r.right
                r.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

def main():
    root = TreeNode(1)
    t1 = TreeNode(2)
    t2 = TreeNode(3)
    t3 = TreeNode(4)
    t4 = TreeNode(5)
    t5 = TreeNode(6)
    root.left = t1
    root.right = t4
    t1.left = t2
    t1.right = t3
    t4.right = t5
    solution = Solution()
    solution.flatten(root)

if __name__ == "__main__":
    main()
