# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = [root]
        depth = 1
        while nodes:
            temp = []
            for node in nodes:
                if not node.left and not node.right:
                    return depth
                else:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            nodes = temp[:]
            depth += 1
        return 0


def main():
    root = TreeNode(1)
    solution = Solution()
    result = solution.minDepth(root=root)
    print(result)


if __name__ == '__main__':
    main()
