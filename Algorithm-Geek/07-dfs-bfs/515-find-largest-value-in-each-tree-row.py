# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def largestValues(self, root: TreeNode) -> [int]:
        result = []
        nodes = [root]
        while nodes:
            temp = []
            max_node = nodes[0]
            for node in nodes:
                if max_node.val < node.val:
                    max_node = node
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            nodes = temp[:]
            result.append(max_node.val)
        return result



def main():
    root = TreeNode(1)
    solution = Solution()
    result = solution.largestValues(root=root)
    print(result)

if __name__ == '__main__':
    main()



