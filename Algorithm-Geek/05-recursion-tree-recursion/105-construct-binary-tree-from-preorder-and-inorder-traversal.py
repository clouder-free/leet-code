# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        return None

def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15,20, 7]
    solution = Solution()
    root = solution.buildTree(preorder=preorder, inorder=inorder)

if __name__ == '__main__':
    main()



