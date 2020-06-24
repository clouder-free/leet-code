#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。
例如，
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        # 根节点
        val = preorder[0]
        root = TreeNode(val)
        root_index = inorder.index(val)
        # 左子树中序
        linorder = inorder[:root_index]
        # 左子树先序
        lpreorder = preorder[1:1+len(linorder)]
        root.left = self.buildTree(preorder=lpreorder, inorder=linorder)
        # 右子树中序
        rinorder = inorder[root_index+1:]
        # 右子树先序
        rpreorder = preorder[-len(rinorder):]
        root.right = self.buildTree(preorder=rpreorder, inorder=rinorder)
        return root

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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    root = solution.buildTree(preorder=preorder, inorder=inorder)
    result = solution.levelOrder(root=root)
    print(result)

if __name__ == "__main__":
    main()
