#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
根据一棵树的中序遍历与后序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。
例如，给出
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
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

    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        # 根节点
        val = postorder[-1]
        root = TreeNode(val)
        root_index = inorder.index(val)
        # 左子树中序
        linorder = inorder[:root_index]
        # 左子树后序
        lpostorder = postorder[:len(linorder)]
        root.left = self.buildTree(inorder=linorder, postorder=lpostorder)
        # 右子树中序
        rinorder = inorder[root_index+1:]
        # 右子树后序
        rpostorder = postorder[-1-len(rinorder):-1]
        root.right = self.buildTree(inorder=rinorder, postorder=rpostorder)
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
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    solution = Solution()
    root = solution.buildTree(inorder=inorder, postorder=postorder)
    result = solution.levelOrder(root=root)
    print(result)

if __name__ == "__main__":
    main()
