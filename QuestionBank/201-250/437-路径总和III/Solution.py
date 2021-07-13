# -*- coding: utf-8 -*-
"""
路径总和III
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def _dfs(node, ps, current):
            if not node:
                return 0
            res = 0
            # 当前路径和
            current += node.val
            res += ps.get(current-targetSum, 0)
            # 更新前缀和
            ps[current] = ps.get(current, 0) + 1
            # 下一层
            res += _dfs(node.left, ps, current)
            res += _dfs(node.right, ps, current)
            # 回到本层
            ps[current] -= 1
            return res
        return _dfs(root, {0: 1}, 0)


def main():
    root = TreeNode(10)
    n1 = TreeNode(5)
    n2 = TreeNode(-3)
    root.left = n1
    root.right = n2
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n1.left = n3
    n1.right = n4
    n5 = TreeNode(11)
    n2.right = n5
    n6 = TreeNode(3)
    n7 = TreeNode(-2)
    n3.left = n6
    n3.right = n7
    n8 = TreeNode(1)
    n4.right = n8
    targetSum = 8
    print(Solution().pathSum(root, targetSum))


if __name__ == '__main__':
    main()
