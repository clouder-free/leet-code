#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
示例:
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def generateTrees(self, n: int) -> [TreeNode]:
        if n == 0:
            return [None]
        def create_tree(start, end):
            trees = []
            if start > end:
                trees.append(None)
            else:
                for i in range(start, end+1):
                    # 构造左子树
                    lefts = create_tree(start=start, end=i-1)
                    # 构造右子树
                    rights = create_tree(start=i+1, end=end)
                    # 组合
                    for left in lefts:
                        for right in rights:
                            root = TreeNode(i)
                            root.left = left
                            root.right = right
                            trees.append(root)
            return trees
        return create_tree(start=1, end=n)


    def levelOrder(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        nodes = [root]
        while nodes:
            level_result = []
            temp = []
            # 输出本层节点 并添加下一层的节点
            for node in nodes:
                level_result.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            result.append(level_result)
            nodes = temp[:]
        return result

def main():
    n = 3
    solution = Solution()
    results = solution.generateTrees(n=3)
    print(len(results))

if __name__ == "__main__":
    main()



