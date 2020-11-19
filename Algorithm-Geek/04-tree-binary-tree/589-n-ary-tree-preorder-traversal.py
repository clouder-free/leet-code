# -*- coding: utf-8 -*-

class Node(object):

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):

    def preorder(self, root: Node) -> [int]:
        result = []
        def recurse(node, lst):
            if node:
                lst.append(node.val)
                for chl in node.children:
                    recurse(chl, lst)
        recurse(root, result)
        return result

    def preorder2(self, root: Node) -> [int]:
        result = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                result.append(root.val)
                for chl in root.children[::-1]:
                    stack.append(chl)
        return result





def main():
    root = Node(val=1)
    solution = Solution()
    result = solution.preorder(root=root)
    print(result)

if __name__ == '__main__':
    main()



