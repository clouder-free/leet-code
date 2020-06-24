#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。
(即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行)。
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：
[
  [3],
  [20,9],
  [15,7]
]
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        nodes = [root]
        # 从左到右输出
        lToR = True
        while nodes:
            level_result = []
            temp = []
            # 输出本层节点 并添加下一层的节点
            for node in nodes:
                if not lToR:
                    level_result = [node.val] + level_result
                else:
                    level_result.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            # 取反
            lToR = bool(1-lToR)
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
    result = solution.zigzagLevelOrder(root=root)
    print(result)

if __name__ == "__main__":
    main()

