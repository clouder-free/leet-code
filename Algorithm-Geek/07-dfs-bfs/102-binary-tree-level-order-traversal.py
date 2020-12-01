# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            temp = []
            res = []
            for node in queue:
                res.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            result.append(res[:])
            queue = temp[:]
        return result

def main():
    root = TreeNode(1)
    solution = Solution()
    result = solution.levelOrder(root=root)
    print(result)

if __name__ == '__main__':
    main()



