# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        i = inorder.index(val)
        # 左子树中序
        li = inorder[:i]
        # 右子树中序
        ri = inorder[i+1:]
        # 左子树先序
        lp = preorder[1:len(li)+1]
        # 右子树先序
        rp = preorder[len(li)+1:]
        root.left = self.buildTree(preorder=lp, inorder=li)
        root.right = self.buildTree(preorder=rp, inorder=ri)
        return root


def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    root = solution.buildTree(preorder=preorder, inorder=inorder)

if __name__ == '__main__':
    main()



