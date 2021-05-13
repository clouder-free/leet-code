# -*- coding: utf-8 -*-

class Node(object):

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):

    def postorder(self, root: Node) -> [int]:
        result = []
        def recursive(node, lst):
            if not node:
                return
            for chld in node.children:
                recursive(chld, lst)
            lst.append(node.val)
        recursive(root, result)
        return result

    def postorder2(self, root: Node) -> [int]:
        result = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                result.append(root.val)
                if root.children:
                    for chl in root.children:
                        stack.append(chl)
        return result[::-1]


def main():
    root = Node(val=1)
    solution = Solution()
    result = solution.postorder2(root=root)
    print(result)

if __name__ == '__main__':
    main()



