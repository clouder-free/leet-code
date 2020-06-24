#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        lefts = [root.left]
        rights = [root.right]
        def is_empty(nodes):
            for node in nodes:
                if node:
                    return False
            else:
                return True

        # 左右都为空时[None] [None]
        while not is_empty(lefts) or not is_empty(rights):
            # 其中一个不为空 判断长度是否相同
            if len(lefts) != len(rights):
                return False
            i = len(lefts) - 1
            while i >= 0:
                j = len(lefts) - 1 - i
                # 其中一个为空 另一个不为空
                if (lefts[i] and not rights[j]) or (not lefts[i] and rights[j]):
                    return False
                # 都为空 或者 两者相等
                if (not lefts[i] and not rights[j]) or (lefts[i].val == rights[j].val):
                    i -= 1
                else:
                    return False
            # 遍历下一层
            # 左子树下一层
            ls = []
            for node in lefts:
                if node:
                    ls.append(node.left)
                    ls.append(node.right)
                else:
                    ls.append(node)
            lefts = ls[:]
            # 右子树下一层
            rs = []
            for node in rights:
                if node:
                    rs.append(node.left)
                    rs.append(node.right)
                else:
                    rs.append(node)
            rights = rs[:]

        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True
        def recurse(node1, node2):
            if not node1 and not node2:
                return True
            # 其中一个为空
            if (node1 and not node2) or (not node1 and node2):
                return False
            # 两者值不相等
            if node1.val != node2.val:
                return False
            return recurse(node1.left, node2.right) and recurse(node1.right, node2.left)
        return recurse(node1=root.left, node2=root.right)

def main():
    root = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(2)
    l4 = TreeNode(3)
    l5 = TreeNode(4)
    l6 = TreeNode(4)
    l7 = TreeNode(3)
    root.left = l2
    root.right = l3
    l2.left = l4
    l2.right = l5
    l3.left = l6
    l3.right = l7
    solution = Solution()
    result = solution.isSymmetric(root=root)
    print(result)

if __name__ == "__main__":
    main()

