# -*- coding: utf-8 -*-
"""
打家劫舍III
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rob(self, root: TreeNode) -> int:
        def rob_back(node, temp):
            if not node:
                return 0
            if node in temp:
                return temp[node]
            money = node.val
            if node.left:
                money += (rob_back(node.left.left, temp) + rob_back(node.left.right, temp))
            if node.right:
                money += (rob_back(node.right.left, temp) + rob_back(node.right.right, temp))
            result = max(money, rob_back(node.left, temp) + rob_back(node.right, temp))
            temp[node] = result
            return result
        return rob_back(root, {})


def main():
    root = TreeNode(3)
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(1)
    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4
    n2.right = n5
    print(Solution().rob(root))


if __name__ == '__main__':
    main()
